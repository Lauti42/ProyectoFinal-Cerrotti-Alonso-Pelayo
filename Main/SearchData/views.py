from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Preferencias_Usuario
from RegistroUsuarios.models import Avatar
from Blog_General.models import Publicacion

# Create your views here.

def buscarPreferencias(request):

    return render(request, 'buscarpreferencias.html')


def resultadoPreferencias(request):
    if request.GET["titulo"]:

        titulo = request.GET["titulo"]
         
        publicacionBody = Publicacion.objects.filter(contenido__contains=titulo)

        return render(request, 'Blog_Generalindex.html', {'buesqueda_posteos': publicacionBody})
    else:

        lenguaje = "No seleccionado"
        return render(request, 'Blog_Generalidex.html', {'lenguaje': lenguaje})


def buscarUsuarios(request):
     pass