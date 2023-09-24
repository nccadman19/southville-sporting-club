import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .utils import determine_country_currency
from .forms import OrderForm
from django.http import JsonResponse
from django.views import View 

from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    user_country = request.session.get('user_country', None)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'user_country': user_country,
    }

    return render(request, template, context)

# Create a separate view for creating the Stripe checkout session
class CreateStripeCheckoutSessionView(View):
    def post(self, request):
        domain_url = 'https://8000-nccadman19-southvillesp-6v9qnrfjhft.ws-eu104.gitpod.io/'
        # Get the shopping cart from the session
        cart = request.session.get('bag', {})
        total_price = 0
        line_items = []

        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            selected_country = order_form.cleaned_data['country']

        for product_id, quantity in cart.items():
            try:
                product_id_without_suffix = product_id.split('_')[0]
                product = Product.objects.get(pk=product_id_without_suffix)
                subtotal = product.price * quantity
                total_price += subtotal

                # Get the currency code based on the country code
                currency = determine_country_currency(selected_country)

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
                        "currency": currency,
                        "unit_amount": int(product.price * 100),
                        "product_data": {
                            "name": product.name,
                            # "images": [absolute_image_url],
                        },
                    },
                    "quantity": quantity,
                })
            except Product.DoesNotExist:
                messages.error(request, "Product not found")

        # Create the Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=domain_url + reverse('checkout_success'),
            cancel_url=domain_url + reverse('checkout_cancel'),
            metadata={"product_id": product_id}, 
        )
        return redirect(checkout_session.url, code=303)


def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')

def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')
