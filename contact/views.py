from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import ContactSubmission

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid!") 
            contact_submission = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact_submission.save()  # Save the data to the database

            send_mail(
                form.cleaned_data['subject'],  # subject
                f"Message from {form.cleaned_data['fname']} {form.cleaned_data['lname']} "
                f"<{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",  # message
                None,  # from email
                ['contact@southvillesportingclub.com'],
            )
            messages.success(
                request,
                'Thank you for submitting! We will be in touch asap!')
            return render(request, 'contact/contact_us.html')

    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})