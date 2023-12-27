from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100, required=True)
    lastname = forms.CharField(label='Last Name', max_length=100, required=False)
    email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Subject', widget=forms.Textarea, required=True)
