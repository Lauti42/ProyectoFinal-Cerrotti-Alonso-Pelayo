import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from RegistroUsuarios.models import Registro_usuarios , Preferencias_Usuario
from RegistroUsuarios.forms import PreferenciasFormulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def registrarse(request):
    return render(request, 'registrarse.html')

def registro(request):
    if request.method == 'POST':
        print("POST")

        form = UserCreationForm(request.POST)
        print(form)

        if form.is_valid(): 
            print("es valido")
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indexBase.html', {'mensaje': f'Usuario Creado {username}'})

    else:

        form = UserCreationForm()

    return render(request, 'registrarse.html', {'form': form})        


        #Obteniendo datos del registro (Form)
        #nombre = request.POST['Usuario']
        #email = request.POST['Email']
        #password = request.POST['Contraseña']
        #password2 = request.POST['Contraseña2']
    
        #Guardando los datos en la DB
        #User_registred = Registro_usuarios(nombre=nombre, email=email, password=password)
        #User_registred.save()
            
        #documentoDeTexto = f"Integrante creado con exito: {nombre} {email} {password} {password2}"
        #return render(request, "indexregistrado.html", {'documentoDeTexto': documentoDeTexto})

def preferencias(request):
    if request.method == "POST":
        print("POST")
        #Obteniendo datos del registro (Form)
        preferenciasUsuarioForm = PreferenciasFormulario(request.POST)    
        
        if preferenciasUsuarioForm.is_valid():

            data = preferenciasUsuarioForm.cleaned_data

            #Guardando los datos en la DB
            Pref = Preferencias_Usuario(lenguaje=data["lenguaje"], backOfront=["backofront"], pais=["pais"], trabajo=["trabajo"])
            Pref.save()

        return render(request, "preferenciasenviadas.html")

def login_request(request):

    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            #email= form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            usuario = form.cleaned_data.get('username')

            user= authenticate(username= usuario, password= password)

            if user:
                login(request, user)
                print("entramos a bienvenido")
                return render(request, 'indexBase.html', {'mensaje': f'Bienvenido {usuario}'})

            else:
                print("entramos a error")
                return render(request, 'indexBase.html', {'mensaje': 'Error, datos incorrectos'})

        return render(request, 'indexBase.html', {'mensaje': 'Error, formulario erroneo'})

    else:  

    
       form= AuthenticationForm()

    return render(request, 'login.html', {'form': form})

                
