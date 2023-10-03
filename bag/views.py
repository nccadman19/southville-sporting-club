from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . import views
from products.models import Product

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
        message = f'Updated {product.name} quantity to {bag[item_id]}'
    else:
        bag[item_id] = quantity
        message = f'Added {product.name} ({selected_size}) to your bag'

    messages.success(request, message)

    request.session['bag'] = bag
    request.session.modified = True  """ Indicate that the session has been modified """
    return redirect(redirect_url)

def remove_item(request, item_id):
    selected_size = request.POST.get('selected_size')

    """ Update the cart in the session """
    bag = request.session.get('bag', {})
    item_id = f"{item_id}_{selected_size}"

    """ Remove one item from bag """
    if item_id in bag:
        if bag[item_id] > 1:
            bag[item_id] -= 1  
        else:
            del bag[item_id]  
        request.session.modified = True

        """ Send a success message to the user """
        messages.success(request, f'Removed one item from your bag')

        return JsonResponse({'status': 'success'})
    else:
        """ If the item was not found in the bag, send an error message """
        return JsonResponse({'status': 'error', 'message': 'Item not found in your bag'})


