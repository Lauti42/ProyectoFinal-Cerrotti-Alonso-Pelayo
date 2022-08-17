from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Preferencias_Usuario
from RegistroUsuarios.models import Avatar

# Create your views here.

def buscarPreferencias(request):

    return render(request, 'buscarpreferencias.html')


def resultadoPreferencias(request):
    if request.GET["lenguaje"]:

        lenguaje = request.GET["lenguaje"]
        preferencias = Preferencias_Usuario.objects.filter(lenguaje__icontains=lenguaje)

        return render(request, 'resultadopreferencias.html', {'preferencias': preferencias, 'lenguaje': lenguaje})
    else:

        lenguaje = "No seleccionado"
        return render(request, 'buscarpreferencias.html', {'lenguaje': lenguaje})


def buscarUsuarios(request):
     pass