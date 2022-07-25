from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from django.urls import include, path
from .views import buscarPreferencias, buscarUsuarios, resultadoPreferencias

urlpatterns = [
    path('preferencias/', buscarPreferencias),
    path('Usuarios/', buscarUsuarios),
    path('preferencias/resultado/', resultadoPreferencias),
    
]
