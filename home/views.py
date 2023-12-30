import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def shipping(request):
    """ A view to return the shipping and returns page """

    return render(request, 'home/shipping_and_returns.html')

def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms_and_conditions.html')

def about(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/about_us.html')

def sustainability(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/sustainability.html')