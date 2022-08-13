import email
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import customuser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm, ContactForm
from .forms import RegistrationForm
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from .models import customuser, Contact
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

def landing(request):
    return render(request, 'landing/landing.html')

def signup(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']

        if customuser.objects.filter(email=email):
            messages.error(request, "Email Already Exists")
            return redirect('/signup')

        newuser = customuser.objects._create_user(email, password)
        newuser.save()
        
        messages.success(request, "Your account has been successfully created")
        return redirect('/login')
     
    return render(request, 'landing/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('prototype:dashboard')
        else:
            messages.error(request, 'Email or Password does not exist')
            return redirect('/login')
    else:
        return render(request, 'landing/login.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Success! Thank you for your message.')
      
	form = ContactForm()
	return render(request, "landing/contact.html", {'form':form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
    return render(request, 'landing/contact.html')

def reset(request):
    return render(request, 'landing/password_reset.html')

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/login')

def support(request):
    return render(request, 'landing/support.html')

def authTable(request):
    return render(request, 'landing/fileAuthen3.html')

def about(request):
    return render(request, 'landing/about_us.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "landing/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return render(request, "landing/password_reset_done.html")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="landing/password_reset.html", context={"password_reset_form":password_reset_form})

