from django.shortcuts import render
from . import views

# Create your views here.

def view_bag(request):
    """ A view to return contents of the users bag """

    return render(request, 'bag/bag.html')