import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Blog_General.models import Publicacion
from Main.settings import MEDIA_URL
from RegistroUsuarios.forms import AvatarFormulario, SignUpForm, UserEditForm
from RegistroUsuarios.models import Avatar

# Create your views here.


def registrarse(request): # Renderizamos la vista de registro
    
    return render(request, 'registrarse.html')

def registro(request): # Obtenemos los datos del usuario por metodo post.
    if not request.user.is_authenticated: # Deslogueamos al usuario en caso de que este conectado antes del registro
        if request.method == 'POST': # Aseguramos que el method utilizado sea Post.
            

            formreg = SignUpForm(request.POST) # Enviamos la request al formulario y lo conservamos en una variable.
        

            if formreg.is_valid(): # Consultamos sobre la validacion del form.
                
                # Guardamos los datos obtenidos al formulario.
                username = formreg.cleaned_data['username']
                formreg.save()
                publicaciones = Publicacion.objects.filter(muestra_inferior="si")
                return render(request, 'IndexBase.html', {'mensaje': f'Bienvenido {username}! tu usuario ha sido creado','posteos':publicaciones})

        else: #Si el method == GET necesitamos renderizar el form de registro en registrarse.html

            formreg = SignUpForm()

        return render(request, 'registrarse.html', {'formreg': formreg}) 
    else:
        return HttpResponseRedirect(reverse('logout'))


def login_request(request):
    
    Publicaciones = Publicacion.objects.filter(muestra_inferior= 'si') #Obtenemos todos los objetos de la Clase Publicacion con un Filtro activado
    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST) 
        

        if form.is_valid():
            
            password = form.cleaned_data.get('password')
            usuario = form.cleaned_data.get('username')

            user= authenticate(username= usuario, password= password) # Autenticamos el usuario
            
            if user: #Si el usuario es True le damos ingreso al sitio y renderizamos el index con los objetos de publicacion obtenidos anteriormente.
                login(request, user)
                print("entramos a bienvenido")
                return render(request, 'indexBase.html', {'mensaje': f'Bienvenido {usuario}', 'posteos': Publicaciones})

            else: # Si el usuario es False lo redirigimos a el HTML Errores con el mensaje correspondiente.
                print("entramos a error")
                return render(request, 'Errores.html', {'mensaje': 'El nombre de usuario o la contraseña son incorrectos', 'posteos': Publicaciones})
        
        return render(request, 'Errores.html', {'mensaje': 'El nombre de usuario o la contraseña son incorrectos', 'posteos': Publicaciones})

    else:  
        
        return render(request, 'indexBase.html', {'posteos': Publicaciones, 'form': AuthenticationForm()})

                
@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':
        print("post")
        miFormulario = UserEditForm(request.POST, instance=request.user) # Enviamos a los formularios Avatar y UserEditForm los datos de la Request.
        formAvatar = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            print("es valido")
            data = miFormulario.cleaned_data
            

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password = data["password1"]

            # Actualizamos los datos obtenidos en la request.
            
            usuario.set_password(usuario.password) 
            usuario.save()
            
 


            '''
            Necesitamos comprobar 3 cosas antes de cargar el avatar ya que el formulario puede 
            devolver None (No cargo archivos).
            1) No tenga Imagen cargada pero si una anterior (Traemos la ultima que tenia.)
            2) No tenga Imagen cargada y tampoco una anterior (Cargamos una IMG defoult.jpg)
            3) Tenga una anterior y la quiera actualizar (Cargamos la nueva imagen)
    
            '''
            if formAvatar.is_valid():
                dataAvatar = formAvatar.cleaned_data
                print(dataAvatar)
                if dataAvatar['imagen'] == None and Avatar.objects.filter(user=request.user.id).last():
                    
                    avatar = Avatar.objects.filter(user=request.user.id).last()
                    avatar.save()
                elif dataAvatar['imagen'] == None and Avatar.objects.filter(user=request.user.id).last() == None:
                    
                    avatar = Avatar(user=request.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg'))
                    avatar.save()
                elif dataAvatar['imagen'] != None:
                    
                    avatar = Avatar(user=request.user, imagen=dataAvatar["imagen"])
                    avatar.save()
            
            return render(request, "indexBase.html", {"mensaje": "Datos actualizados con éxito..."}) #Devolvemos un mensaje de Exito
        return render(request, "indexBase.html", {"mensaje": "La contraseña es invalida, Debe contener minimo 8 Caracteres alfanumericos y ambas deben coinicidir"}) #Si las contraseñas no coinciden o son solamente numeros
    else:

        miFormulario = UserEditForm(instance=request.user)         #Caso contrario , devolvemos los formularios correspondientes a modificar_perfil
        formAvatar = AvatarFormulario()    
        Posteos = Publicacion.objects.filter(user=request.user)
        context = miFormulario.errors
    return render(request, "modificar_perfil.html", {"miFormulario": miFormulario, "formAvatar": formAvatar, "Posteos": Posteos, 'context':context})


        