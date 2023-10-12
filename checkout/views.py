from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.sessions.models import Session
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View 
from random import randint
from datetime import datetime
from django.db import transaction

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import json
import stripe
import os

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    bag = request.session.get('bag', {})

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)

def generate_order_number():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_component = str(randint(1000, 9999))
    return f'ORDER-{timestamp}-{random_component}'

class CreateStripeCheckoutSessionView(View):
    def post(self, request):
        # Initialize the list to store OrderLineItem instances to save later
        order_line_items_to_save = []

        domain_url = 'https://8000-nccadman19-southvillesp-vyffy813txj.ws-eu105.gitpod.io'
        # Get the shopping cart from the session
        cart = request.session.get('bag', {})
        total_price = 0
        line_items = []

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        delivery_cost = float(request.POST.get('delivery_cost', '0.00'))
        print('delivery_cost', delivery_cost)

        # Validate the form before accessing cleaned_data
        if order_form.is_valid():
            # Access cleaned_data here
            customer_email = order_form.cleaned_data['email']

        for product_id, quantity in cart.items():
            try:
                product_id_without_suffix = product_id.split('_')[0]
                product = Product.objects.get(pk=product_id_without_suffix)
                subtotal = product.price * quantity
                total_price += subtotal

                # Ensure quantity is a positive integer
                try:
                    quantity = int(quantity)
                    if quantity <= 0:
                        raise ValueError()
                except ValueError:
                    messages.error(request, "Invalid quantity selected")
                    return redirect(reverse('checkout'))

                # Append the line item to the line_items list
                line_items.append({
                    "price_data": {
                        "unit_amount": int(product.price * 100),
                        "currency": "GBP",
                        "product_data": {
                            "name": product.name,
                        },
                    },
                    "quantity": quantity,
                })

            except Product.DoesNotExist:
                messages.error(request, "Product not found")
        
        # Add a line item for delivery
        line_items.append({
            "price_data": {
                "unit_amount": int(delivery_cost * 100),
                "currency": "GBP",
                "product_data": {
                    "name": "Delivery",
                },
            },
            "quantity": 1, 
        })

        # Generate a unique order number for this order
        order_number = generate_order_number()

        # Create the Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            customer_email=order_form.cleaned_data['email'],
            mode="payment",
            success_url=domain_url + reverse('checkout_success', args=[order_number]),
            cancel_url=domain_url + reverse('checkout_cancel'),
        )

        # Store delivery_cost in the session
        request.session['delivery_cost'] = delivery_cost

        # Check if the Stripe payment is successful
        if checkout_session.payment_status == "paid":
            for line_item in order_line_items_to_save:
                line_item.order = order

        # Save order data to your database after successful payment
        with transaction.atomic():
            order = Order.objects.create(
                order_number=order_number,
                full_name=order_form.cleaned_data['full_name'],
                email=order_form.cleaned_data['email'],
                phone_number=order_form.cleaned_data['phone_number'],
                postcode=order_form.cleaned_data['postcode'],
                town_or_city=order_form.cleaned_data['town_or_city'],
                street_address1=order_form.cleaned_data['street_address1'],
                street_address2=order_form.cleaned_data['street_address2'],
            )

            for line_item in order_line_items_to_save:
                line_item.order = order
                line_item.save()
            
        context = {
            'order': order,
        }

        return redirect(checkout_session.url, code=303)

def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    save_info = request.session.get('save_info')
    # Retrieve the delivery_cost from the session
    delivery_cost = request.session.get('delivery_cost', 0.00)
    print('delivery_cost', delivery_cost)

    # Store the bag items as line items in the order
    for item_key, quantity in request.session.get('bag', {}).items():
        product_id, selected_size = item_key.split('_')

        try:
            product = Product.objects.get(pk=product_id)
            subtotal = product.price * quantity

            # Create OrderLineItem instance and append it to the order
            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                lineitem_total=subtotal,
                product_size=selected_size,
            )

        except Product.DoesNotExist:
            messages.error(request, "Product not found")

    profile = UserProfile.objects.get(user=request.user)

    # Update the delivery_cost field in the Order instance and save it
    order.delivery_cost = delivery_cost
    order.save()

    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Clear the bag from the session
    request.session['bag'] = {}
    request.session.modified = True

    context = {
        'order': order,
        'delivery_cost': delivery_cost,
    }

    return render(request, 'checkout/checkout_success.html', context)

def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')