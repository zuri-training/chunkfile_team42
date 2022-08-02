from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())


def login_view(request):
    return render(request, 'login.html')


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
