from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from RegistroUsuarios.models import Registro_usuarios , Preferencias_Usuario
# Create your views here.
def indexview(request):
    return render(request, 'indexBase.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def registro(request):
    if request.method == 'POST':
        print("POST")

        #Obteniendo datos del registro (Form)
        nombre = request.POST['Usuario']
        email = request.POST['Email']
        password = request.POST['Contraseña']
        password2 = request.POST['Contraseña2']

        #Guardando los datos en la DB
        User_registred = Registro_usuarios(nombre=nombre, email=email, password=password)
        User_registred.save()
            
        documentoDeTexto = f"Integrante creado con exito: {nombre} {email} {password} {password2}"
        return render(request, "indexregistrado.html", {'documentoDeTexto': documentoDeTexto})

def preferencias(request):
    if request.method == "POST":
        print("POST")
        #Obteniendo datos del registro (Form)
        
        lenguaje = request.POST['Lenguaje']
        backOfront = request.POST['BackFront']
        pais = request.POST['Pais']
        trabajo = request.POST['Trabajo']

        #Guardando los datos en la DB
        Pref = Preferencias_Usuario(lenguaje=lenguaje, backOfront=backOfront, pais=pais, trabajo=trabajo)
        Pref.save()

        return render(request, "preferenciasenviadas.html")
