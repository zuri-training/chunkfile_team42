from django import forms
from .models import customuser, customuserManager
from django.contrib.auth.forms import UserCreationForm
from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = customuser
        fields = ["fullname", "email", "password"]

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fullname': TextInput(attrs={
                'class': "inp",
                'style': 'width: 400px;',
                'placeholder': 'Full Name'
                }),
            'email': EmailInput(attrs={
                'class': "inp", 
                'style': 'max-width: 400px;',
                'placeholder': 'Email Address'
                }),
            'message': TextInput(attrs={
                'class': "inp", 
                'style': 'max-width: 400px; padding-bottom:12rem;',
                'placeholder': 'message'
                })
            
        }
