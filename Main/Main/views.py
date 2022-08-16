from django.shortcuts import render
from django.http import HttpResponse
from Blog_General.models import Entry
from RegistroUsuarios.views import login_request
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Avatar

def indexview(request):

    posteos = Entry.objects.filter(muestra_inferior= 'si')
    avatar = Avatar.objects.get(user=request.user.id)
    form = AuthenticationForm()
    
    return render(request, 'indexBase.html', {'posteos': posteos, 'form': form, "url": avatar.imagen.url})

def aboutview(request):
    form = AuthenticationForm()
    avatar = Avatar.objects.get(user=request.user.id)
    return render(request, 'about.html', {'form': form, "url": avatar.imagen.url})

def contactview(request):
    avatar = Avatar.objects.get(user=request.user.id)
    form = AuthenticationForm()
    return render(request, 'contact.html', {'form': form, "url": avatar.imagen.url})



        
        