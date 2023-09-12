from django.shortcuts import render
from . import views

# Create your views here.

def view_bag(request):
    """ A view to return contents of the users bag """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add item to the bag, add only 1 item initially """

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
    