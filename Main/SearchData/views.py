from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Preferencias_Usuario

# Create your views here.

def buscarPreferencias(request):
    form = AuthenticationForm()
    return render(request, 'buscarpreferencias.html', {'form': form})


def resultadoPreferencias(request):
    if request.GET["lenguaje"]:

        lenguaje = request.GET["lenguaje"]
        preferencias = Preferencias_Usuario.objects.filter(lenguaje__icontains=lenguaje)
        form = AuthenticationForm()
        return render(request, 'resultadopreferencias.html', {'preferencias': preferencias, 'lenguaje': lenguaje, 'form': form})
    else:
        lenguaje = "No seleccionado"
        return render(request, 'buscarpreferencias.html', {'lenguaje': lenguaje})


def buscarUsuarios(request):
     pass