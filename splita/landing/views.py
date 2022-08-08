from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import customuser
from django.contrib.auth.decorators import login_required
from django.urls import reverse

##test
#@login_required(login_url='/login') this code would be used when the user wants to acess their dashboard
def landing(request):
    return render(request, 'landing/landing.html')
##endoftest

def signup(request):
    return render(request, 'landing/signup.html')

def adduser(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']

        if customuser.objects.filter(email=email):
            messages.error(request, "Email Already Exists")
            return redirect('/signup')

        newuser = customuser.objects._create_user(email, password, fullname)
        newuser.save()

        messages.success(request, "Your account has been successfully created")
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'landing/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/landing')
        else:
            messages.error(request, 'Email or Password does not exist')
    else:
        return render(request, 'landing/login.html')


def dashboard(request):
    return render(request, 'landing/dashboard.html')
    
def contact(request):
    return render(request, 'landing/contact.html')

def reset(request):
    return render(request, 'landing/reset.html')

def support(request):
    return render(request, 'landing/support.html')
    
    
def authTable(request):
    return render(request, 'landing/fileAuthen3.html')
