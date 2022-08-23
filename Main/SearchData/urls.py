from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from django.urls import include, path
from .views import buscarPreferencias, buscarUsuarios, resultadoPreferencias

urlpatterns = [
    
    path('preferencias/resultado/', resultadoPreferencias, name='resultadopref'),
    
]
