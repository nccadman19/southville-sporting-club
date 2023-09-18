from django.shortcuts import render, redirect, reverse
from checkout.utils import determine_country_from_postcode
from django.contrib import messages
from .forms import OrderForm

def collect_postcode(request):
    if request.method == 'POST':
        user_postcode = request.POST.get('postcode')
        user_country = determine_country_from_postcode(user_postcode)
        
        # Calculate shipping cost and other logic based on user_country
        
        # Redirect to the next step in the checkout process
        return redirect(reverse('checkout:next_step'))
    
    return render(request, 'checkout/collect_postcode.html')

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