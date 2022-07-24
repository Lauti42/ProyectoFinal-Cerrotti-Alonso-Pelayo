from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path 
from RegistroUsuarios.views import indexview, registro , registrarse


urlpatterns = [
    path('', indexview),
    path('registrado/', registro,  name='registrado'),
    path('registrarse/', registrarse, name='registrarse'),
]
