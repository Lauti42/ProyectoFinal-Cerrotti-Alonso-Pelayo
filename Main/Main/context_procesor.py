from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Avatar
from Main.settings import BASE_DIR,MEDIA_URL
import os

def getUserInfo(request):
    
    context = {}
    if not request.user.is_authenticated:
        context['formAuth'] = AuthenticationForm()
        
    else:
        avatar = Avatar.objects.filter(user=request.user.id).last()
        if avatar:
            context['url'] = avatar.imagen.url
        else:
            avatar = Avatar(user=request.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg'))
        context['url'] = avatar.imagen.url 
    
        
    return context

