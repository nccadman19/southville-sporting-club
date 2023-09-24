import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .utils import determine_country_currency
from .forms import OrderForm
from django.http import JsonResponse
from django.views import View 
from random import randint
from datetime import datetime

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

def generate_order_number():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_component = str(randint(1000, 9999))
    return f'ORDER-{timestamp}-{random_component}'

# Create a separate view for creating the Stripe checkout session
class CreateStripeCheckoutSessionView(View):
    def post(self, request):
        domain_url = 'https://8000-nccadman19-southvillesp-6v9qnrfjhft.ws-eu104.gitpod.io'
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
                            # "images": [absolute_image_url],
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
            metadata={"order_number": order_number}, 
        )
        return redirect(checkout_session.url, code=303)


def checkout_success(request):
    # Retrieve the order number from the query parameters in the URL
    order_number = request.GET.get('order_number')

    context = {
        'order_number': order_number,
    }

    return render(request, 'checkout/checkout_success.html', context)


def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')

@csrf_exempt
def stripe_webhook(request):
    # Verify that the request is coming from Stripe using the secret
    webhook_secret = settings.WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle specific webhook events
    if event['type'] == 'payment_intent.succeeded':
        # Handle successful payment
        order_number = event['data']['object']['metadata']['order_number']

    elif event['type'] == 'payment_intent.payment_failed':
        # Handle failed payment
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    return HttpResponse(status=200)
