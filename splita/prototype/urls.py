from unicodedata import name
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
    path('fileAuthen3/', views.fileAuthen3, name='fileAuthen3'),
    path('download_file/', views.download_file, name='download_file'),
    path('myfile/', views.myfile, name='myfile'),
    path('delete/', views.delete, name='delete'),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


