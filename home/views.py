from django.shortcuts import render

# Create your views here.

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
    """ A view to return the terms and conditions page """
    if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        message = request.POST.get('subject')

        # Validate and process the form data
        if not name or not email or not message:
            messages.error(request, "Please fill in all the required fields.")

        # Process the form data and send an email

        # After successful processing
        messages.success(request, "Your message has been sent successfully.")
        return redirect('index')
    return render(request, 'home/contact_us.html')

def sustainability(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/sustainability.html')

def error(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/error.html')