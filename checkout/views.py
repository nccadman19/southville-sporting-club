from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from decimal import Decimal

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed'
            'right now. Please try again later.'
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # Empty string to gather form data
            form_data = {}

            # Don't save it to the database yet
            order = order_form.save(commit=False)

            # Calculate the delivery cost
            delivery_cost = Decimal(request.POST.get('delivery_cost', '0.00'))

            # Set the delivery cost on the order
            order.delivery_cost = delivery_cost

            order.save()  # Now, save the order to the database

            grand_total = Decimal(request.POST.get('grand_total', '0.00'))

            # Store the bag items as line items in the order
            for item_key, quantity in request.session.get('bag', {}).items():
                product_id, selected_size = item_key.split('_')
                try:
                    product = Product.objects.get(pk=product_id)
                    subtotal = product.price * quantity
                    # OrderLineItem instance and append it to the order
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        lineitem_total=subtotal,
                        product_size=selected_size,
                    )
                    # Decrement item quantity in the bag
                    if product_id in request.session['bag']:
                        request.session['bag'][product_id] -= quantity
                        if request.session['bag'][product_id] <= 0:
                            del request.session['bag'][product_id]
                except Product.DoesNotExist:
                    messages.error(request, "Product not found")

            return redirect(
                reverse(
                    'checkout_success',
                    args=[order.order_number]
                )
            )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double-check your information.')
    elif not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    # Only create the 'intent' if you are in the correct code path
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Attempt to prefill the form with any info the
    # user maintains in their profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    # Check if the bag is empty and do not display the form
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret if intent else '',
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Iterate through the order line items and update the product quantities
    for line_item in order.lineitems.all():
        product = line_item.product
        product_size = line_item.product_size
        quantity = line_item.quantity

        # Update the product size quantity in your database
        if product_size in product.size_quantity:
            product.size_quantity[product_size] -= quantity
            product.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
