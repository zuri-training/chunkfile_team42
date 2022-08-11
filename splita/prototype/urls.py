from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('storage/', views.storage, name='storage'),
    path('dashboard/splita/', views.splita, name='splita'),
]
