from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path 
from RegistroUsuarios.views import registro , registrarse, preferencias, login_request, editar_perfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('registrado/', registro,  name='registrado'),
    path('registrarse/', registrarse, name='registrarse'),
    path('preferencias_enviadas/', preferencias, name='preferencias'),
    path('modificar_perfil/', editar_perfil, name='modperfil'),
    
]
