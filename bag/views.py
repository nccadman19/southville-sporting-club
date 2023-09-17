from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from . import views
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return contents of the users bag """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add item to the bag, add only 1 item initially """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    selected_size = request.POST.get('selected_size')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    item_id = f"{item_id}_{selected_size}"
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    message = f'Added {product.name} ({selected_size}) to your bag'
    messages.success(request, message)

    request.session['bag'] = bag
    return redirect(redirect_url)