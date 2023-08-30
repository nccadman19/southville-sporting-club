from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def shipping(request):
    """ A view to return the shipping and returns page """

    return render(request, 'home/shipping-and-returns.html')

def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms-and-conditions.html')

