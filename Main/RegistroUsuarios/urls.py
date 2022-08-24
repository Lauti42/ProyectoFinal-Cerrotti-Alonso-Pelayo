
from django.urls import path

from RegistroUsuarios.views import (editar_perfil, registrarse,
                                    registro)

urlpatterns = [
    
    path('registrado/', registro,  name='registrado'),
    path('registrarse/', registrarse, name='registrarse'),
    path('modificar_perfil/', editar_perfil, name='modperfil'),
    
    
]
