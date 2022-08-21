import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from Main.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from RegistroUsuarios.models import Registro_usuarios , Preferencias_Usuario
from RegistroUsuarios.forms import PreferenciasFormulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from RegistroUsuarios.forms import AvatarFormulario , UserEditForm
from django.contrib.auth.decorators import login_required
from RegistroUsuarios.models import Avatar
from Blog_General.models import Publicacion
import os
# Create your views here.


def registrarse(request):
    
    return render(request, 'registrarse.html')

def registro(request):
    if request.method == 'POST':
        print("POST")

        formreg = UserCreationForm(request.POST)
       

        if formreg.is_valid(): 
            
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
            avatar = Avatar.objects.get(user=request.user.id)

            #Guardando los datos en la DB
            Pref = Preferencias_Usuario(lenguaje=data["lenguaje"], backOfront=["backofront"], pais=["pais"], trabajo=["trabajo"])
            Pref.save()
        form = AuthenticationForm()
        return render(request, "preferenciasenviadas.html", {'form': form})

def login_request(request):
    
    Publicaciones = Publicacion.objects.filter(muestra_inferior= 'si')
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
                return render(request, 'indexBase.html', {'mensaje': f'Bienvenido {usuario}', 'posteos': Publicaciones})

            else:
                print("entramos a error")
                return render(request, 'Errores.html', {'mensaje': 'El nombre de usuario o la contraseña son incorrectos', 'posteos': Publicaciones})
        
        return render(request, 'Errores.html', {'mensaje': 'El nombre de usuario o la contraseña son incorrectos', 'posteos': Publicaciones})

    else:  
        
        return render(request, 'indexBase.html', {'posteos': Publicaciones, 'form': AuthenticationForm()})

                
@login_required
def editar_perfil(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)
        formAvatar = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
             
            data = miFormulario.cleaned_data
            

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password = data["password1"]

            usuario.set_password(usuario.password) 
            usuario.save()

            if formAvatar.is_valid():
                dataAvatar = formAvatar.cleaned_data
                print(dataAvatar)
                if dataAvatar['imagen'] == None and Avatar.objects.filter(user=request.user.id).last():
                    print("entramos a sin imagen pero con una anterior")
                    avatar = Avatar.objects.filter(user=request.user.id).last()
                    avatar.save()
                elif dataAvatar['imagen'] == None and Avatar.objects.filter(user=request.user.id).last() == None:
                    print("entramos a sin imagen y sin una anterior")
                    avatar = Avatar(user=request.user, imagen=os.path.join(BASE_DIR, 'img/default.jpg'))
                    avatar.save()
                elif dataAvatar['imagen'] != None:
                    print("entramos con imagen")
                    avatar = Avatar(user=request.user, imagen=dataAvatar["imagen"])
                    avatar.save()
            
            return render(request, "indexBase.html", {"mensaje": "Datos actualizados con éxito..."})
    else:

        miFormulario = UserEditForm(instance=request.user)
        formAvatar = AvatarFormulario()    
        Posteos = Publicacion.objects.filter(user=request.user)

    return render(request, "modificar_perfil.html", {"miFormulario": miFormulario, "formAvatar": formAvatar, "Posteos": Posteos})


        