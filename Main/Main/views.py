from django.shortcuts import render
from django.http import HttpResponse
from Blog_General.models import Entry
from RegistroUsuarios.views import login_request
from django.contrib.auth.forms import AuthenticationForm

def indexview(request):

    posteos = Entry.objects.filter(muestra_inferior= 'si')
    form = AuthenticationForm()
    return render(request, 'indexBase.html', {'posteos': posteos, 'form': form})

def aboutview(request):
    form = AuthenticationForm()
    return render(request, 'about.html', {'form': form})

def contactview(request):
    form = AuthenticationForm()
    return render(request, 'contact.html', {'form': form})


def indexLogin(request):
    form = AuthenticationForm()
    return render(request, 'indexBaseLogin.html', {'form': form})

        
        