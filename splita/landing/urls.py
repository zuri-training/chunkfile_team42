from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('reset/', views.reset, name='reset'),
    path('support/', views.support, name='support'),
    path('adduser/', views.adduser, name='adduser'),
    path('authTable/', views.authTable, name='authTable'),
]
