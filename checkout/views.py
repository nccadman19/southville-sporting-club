from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
from decimal import Decimal

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {}) 

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # Empty string to gather form data
            form_data = {}

            # Gather form data if form valid 
            for field in OrderForm.Meta.fields:
                form_data[field] = request.POST.get(field, '')

            order = order_form.save(commit=False)  # Don't save it to the database yet

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

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double-check your information.')
    else:
        if not bag:
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

    # Check if the bag is empty and do not display the form
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()

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
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')