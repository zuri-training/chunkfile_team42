from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    # path('reset/', views.reset, name='reset'),
    path('logout/',views.logoutview,name='logout'),
    path('support/', views.support, name='support'),
    path('authTable/', views.authTable, name='authTable'),
    path('about/', views.about, name='about'),
     path("password_reset/", views.password_reset_request, name="password_reset")

]
