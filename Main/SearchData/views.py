from django.http import HttpResponse
from django.shortcuts import render

from RegistroUsuarios.models import Preferencias_Usuario

# Create your views here.

def buscarPreferencias(request):
    return render(request, 'buscarpreferencias.html')


def resultadoPreferencias(request):
    if request.GET["lenguaje"]:

        lenguaje = request.GET["lenguaje"]
        preferencias = Preferencias_Usuario.objects.filter(lenguaje__icontains=lenguaje)

        return render(request, 'resultadopreferencias.html', {'preferencias': preferencias})

def buscarUsuarios(request):
    pass