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

from .utils import determine_country_currency
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
from .stripe_utils import get_metadata_from_stripe

import json
import stripe
import os

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)

def generate_order_number():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_component = str(randint(1000, 9999))
    return f'ORDER-{timestamp}-{random_component}'

# Create a separate view for creating the Stripe checkout session
class CreateStripeCheckoutSessionView(View):
    def post(self, request):
        domain_url = 'https://8000-nccadman19-southvillesp-6v9qnrfjhft.ws-eu105.gitpod.io'
        # Get the shopping cart from the session
        cart = request.session.get('bag', {})
        total_price = 0
        line_items = []

        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            selected_country = order_form.cleaned_data['country']
        
        # Get the currency code based on the country code
        currency = determine_country_currency(selected_country)

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

                line_items.append({
                    "price_data": {
                        "unit_amount": int(product.price * 100),
                        "currency": currency, 
                        "product_data": {
                            "name": product.name,
                        },
                    },
                    "quantity": quantity,
                })
            except Product.DoesNotExist:
                messages.error(request, "Product not found")

        # Generate a unique order number for this order
        order_number = generate_order_number()

        # Create the Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            customer_email=order_form.cleaned_data['email'],
            currency=currency,
            mode="payment",
            success_url=domain_url + reverse('checkout_success'),
            cancel_url=domain_url + reverse('checkout_cancel'), 
            metadata={
                'order_number': order_number,
                'name': order_form.cleaned_data['full_name'],
                'street1': order_form.cleaned_data['street_address1'],
                'street2': order_form.cleaned_data['street_address2'],
                'city': order_form.cleaned_data['town_or_city'],
                'postcode': order_form.cleaned_data['postcode'],
                'phone': order_form.cleaned_data['phone_number'],
            },
        )
        # Get the session ID
        session_id = checkout_session.id
        return redirect(checkout_session.url, code=303)

def checkout_success(request):
    # Retrieve the session_id from the user's session
    session_id = request.session.get('checkout_session_id')

    # Check if session_id is present
    if not session_id:
        # Handle the case where the session_id is missing, e.g., redirect to an error page
        return HttpResponse("Session ID not found")
    
    # Access line_items and amount_total from the request.POST data
    line_items = request.POST.get('line_items')
    amount_total = request.POST.get('amount_total')

    metadata = get_metadata_from_stripe(session_id)

    # Clear the session items from the bag after a successful checkout
    request.session.pop('bag', None)

    context = {
        'metadata': metadata,
        'line_items': line_items,
        'amount_total': amount_total,
    }

    return render(request, 'checkout/checkout_success.html', context)



def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')