from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Avatar

def getUserInfo(request):
    
    context = {}
    if not request.user.is_authenticated:
        context['formAuth'] = AuthenticationForm()

    else:
        avatar = Avatar.objects.filter(user=request.user.id).last()
        context['url'] = avatar.imagen.url if avatar else None
        print(context)
    
    return context

