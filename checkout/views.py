from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

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
