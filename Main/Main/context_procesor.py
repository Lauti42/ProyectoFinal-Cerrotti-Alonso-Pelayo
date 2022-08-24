import os

from django.contrib.auth.forms import AuthenticationForm

from Main.settings import MEDIA_URL
from RegistroUsuarios.models import Avatar


# Definimos una funcion que se encargue de pasar como contexto el Avatar y el Login en toda la web.
def getUserInfo(request):
    
    context = {}
    if not request.user.is_authenticated:
        context['formAuth'] = AuthenticationForm()
        
    else: #Solicitamos el ultimo avatar y lo pasamos como context
        avatar = Avatar.objects.filter(user=request.user.id).last() 
        if avatar: 
            context['url'] = avatar.imagen.url
        else: # Caso contrario, asignamos una imagen Defoult.
            avatar = Avatar(user=request.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg'))
        context['url'] = avatar.imagen.url 
    
        
    return context

