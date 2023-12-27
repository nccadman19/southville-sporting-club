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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['subject']

            messages.success(request, "Your message has been sent successfully.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})

def sustainability(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/sustainability.html')