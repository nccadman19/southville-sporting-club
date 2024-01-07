from django import forms


class ContactForm(forms.Form):
    """ A form for the users contact information """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
