from django import forms
from .models import customuser, customuserManager
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = customuser
        fields = ["fullname", "email", "password"]
