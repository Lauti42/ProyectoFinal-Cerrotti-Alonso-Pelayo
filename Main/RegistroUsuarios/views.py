import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from RegistroUsuarios.models import Registro_usuarios , Preferencias_Usuario
from RegistroUsuarios.forms import PreferenciasFormulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from RegistroUsuarios.forms import AvatarFormulario , UserEditForm
from django.contrib.auth.decorators import login_required
from RegistroUsuarios.models import Avatar
# Create your views here.


def registrarse(request):
    return render(request, 'registrarse.html')

def registro(request):
    if request.method == 'POST':
        print("POST")

        formreg = UserCreationForm(request.POST)
        
        if formreg.is_valid(): 
            print("es valido")
            username = formreg.cleaned_data['username']
            formreg.save()
            return render(request, 'indexregistrado.html', {'mensaje': f'Bienvenido {username}! tu usuario ha sido creado'})

    else:

        formreg = UserCreationForm()
        form = AuthenticationForm()
    return render(request, 'registrarse.html', {'formreg': formreg, 'form': form})    



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
        form = AuthenticationForm()
        return render(request, "preferenciasenviadas.html", {'form': form})

def login_request(request):
    print("entramos a login request")
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
                return render(request, 'Errores.html', {'mensaje': 'Error, datos incorrectos'})

        return render(request, 'Errores.html', {'mensaje': 'Error, formulario erroneo'})

    else:  

    
       form = AuthenticationForm()

    return render(request, 'indexBase.html', {'form': form})

                
@login_required
def editar_perfil(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)
        miAvatar = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid() and miAvatar.is_valid():

            data = miFormulario.cleaned_data
            avatarData = miAvatar.cleaned_data
        
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password = data["password1"]

            usuario.set_password(usuario.password) 
            usuario.save()

            avatar = Avatar(user=request.user, imagen=avatarData['imagen'])
            avatar.save()
        
            return render(request, "indexBase.html", {"mensaje": "Datos actualizados con éxito..."})
    else:

        miFormulario = UserEditForm(instance=request.user)
        miAvatar = AvatarFormulario()

    return render(request, "modificar_perfil.html", {"miFormulario": miFormulario, "miAvatar": miAvatar})

