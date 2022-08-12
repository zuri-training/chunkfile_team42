from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin
app_name = 'prototype'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/splita/', views.splita, name='splita'),
    path('fileAuthen3/', views.MyFilesView.as_view(), name='fileAuthen3'),
    path('filepage/', views.MyFilesView.as_view(), name='filepage'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


