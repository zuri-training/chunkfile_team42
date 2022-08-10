import email
from django import forms
from .models import customuser

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = customuser
        fields = ["fullname", "email", "password"]


class ContactForm(forms.Form):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)