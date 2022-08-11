from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/splita/', views.splita, name='splita'),
    path('fileAuthen/', views.fileAuthen, name='fileAuthen'),
]
