from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from RegistroUsuarios.models import Registro_usuarios

# Create your views here.
def indexview(request):
    return render(request, 'indexBase.html')

def registrarse(request):
    return render(request, 'registrarse.html')

