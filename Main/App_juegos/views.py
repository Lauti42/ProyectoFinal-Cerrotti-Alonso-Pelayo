from django.shortcuts import render
from .models import Desarrollador, Genero, Juegos, Plataformas, ComentarioG 
from .forms import CreaJuegos, NewCommentFormG
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.http import HttpResponse
from RegistroUsuarios.models import Avatar
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from Blog_General.models import Publicacion
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# ---------------------MODELO DESARROLLADOR-------------------
class DesarrolladorList(ListView):
    
    model = Desarrollador
    template_name = "lista-desarrolladores.html"
    context_object_name= 'desarrollador'

class DesarrolladorDetail(DetailView):
    model = Desarrollador
    template_name = "detalle-desarrollador.html"
    context_object_name= 'desarrollador'

class DesarrolladorCreate(LoginRequiredMixin, CreateView):
    model = Desarrollador
    template_name = "crea-desarrollador.html"
    fields = ["nombre", "pais"]
    success_url = "/juegos/desarrolladores/"

class DesarrolladorUpdate(UpdateView):
    model = Desarrollador
    template_name = "edita-desarrollador.html"
    fields = ('__all__')
    success_url = "/juegos/desarrolladores/"

class Desarrolladordelete(DeleteView):
    model = Desarrollador
    template_name = "eliminar-desarrollador.html"
    success_url = "/juegos/desarrolladores/"

def buscardesarrollador(request): 

    if request.GET["desarrollador"]:

        desarrollador = request.GET["desarrollador"]

        desarrolladores = Desarrollador.objects.filter(nombre__icontains=desarrollador)

        return render (request, "resultadoBusqueda.html", {"desarrolladores": desarrolladores, "nombre": desarrollador})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)

    path('buscar-genero', buscargenero, name="BuscarGenero"),

# ---------------------MODELO GENERO-------------------
class GeneroList(ListView):
    
    model = Juegos
    template_name = "lista-generos.html"
    context_object_name= 'generos'

class GeneroDetail(DetailView):
    model = Genero
    template_name = "detalle-genero.html"
    context_object_name= 'generos'

class GeneroCreate(LoginRequiredMixin, CreateView):
    model = Genero
    template_name = "crea-genero.html"
    fields = ["nombre"]
    success_url = "/juegos/generos/"

class GeneroUpdate(UpdateView):
    model = Genero
    template_name = "edita-genero.html"
    fields = ('__all__')
    success_url = "/juegos/generos/"
class Generodelete(DeleteView):
    model = Genero
    template_name = "eliminar-genero.html"
    success_url = "/juegos/generos/"

def buscargenero(request): 

    if request.GET["genero"]:

        genero = request.GET["genero"]

        generos = Genero.objects.filter(nombre__icontains=genero)

        #juegos = Juegos.objects.filter(genero__icontains=generos)

        return render (request, "resultadoBusqueda.html", {"nombre": genero})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)


    path('buscar-plataforma', buscarplataforma, name="BuscarPlataforma"),

# ---------------------MODELO PLATAFORMAS-------------------

class PlataformasList(ListView):
    
    model = Plataformas
    template_name = "lista-plataformas.html"
    context_object_name= 'plataformas'

class PlataformasDetail(DetailView):
    model = Plataformas
    template_name = "detalle-plataforma.html"
    context_object_name= 'plataformas'

class PlataformasCreate(LoginRequiredMixin, CreateView):
    model = Plataformas
    template_name = "crea-plataforma.html"
    fields = ["nombre", "link"]
    success_url = "/juegos/plataformas/"

class PlataformasUpdate(UpdateView):
    model = Plataformas
    template_name = "edita-plataforma.html"
    fields = ('__all__')
    success_url = "/juegos/plataformas/"
class Plataformasdelete(DeleteView):
    model = Plataformas
    template_name = "eliminar-plataforma.html"
    success_url = "/juegos/plataformas/"

def buscarplataforma(request): 

    if request.GET["plataforma"]:

        plataforma = request.GET["plataforma"]

        plataformas = Juegos.objects.filter(nombre__icontains=plataforma)

        return render (request, "resultadoBusqueda.html", {"plataformas": plataformas, "nombre": plataforma})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)

    path('buscar-desarrollador', buscardesarrollador, name="BuscarDesarrollador"),

# ---------------------MODELO JUEGOS-------------------

class JuegosList(ListView):
    
    model = Juegos
    template_name = "iniciojuegos.html"
    context_object_name= 'juegos'

def iniciojuegos(self):

    juegos = Juegos.objects.all()
    generos = Genero.objects.all()
    desarrolladores = Desarrollador.objects.all()
    plataformas = Plataformas.objects.all()

    return render(self, "iniciojuegos.html", {"juegos": juegos, "generos": generos, "desarrolladores": desarrolladores, "plataformas": plataformas})

class JuegosDetail(DetailView):
    model = Juegos
    context_object_name = 'juegos'
    template_name = 'GeneralPostG.html'
    

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = ComentarioG.objects.filter(blogpost_connected= self.get_object()).order_by('-date_added')
        data['comments']= comments_connected
        stuff= get_object_or_404(Juegos, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        data['total_likes']= total_likes

        if self.request.user.is_authenticated:
            data['comment_form']= NewCommentFormG(instance=self.request.user)
            
        return data

    def post(self, request, *args, **kwargs):
        new_comment= ComentarioG(body= request.POST.get('body'), 
            user= self.request.user,
            blogpost_connected= self.get_object())
        
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


def blog_general_indexG(request):

    listado_posts= Juegos.objects.all().order_by('-id')
    paginator= Paginator(listado_posts, 6)
    pagina= request.GET.get('page') or 1
    posts= paginator.get_page(pagina)
    pagina_actual= int(pagina)
    paginas= range(1, posts.paginator.num_pages + 1)


    
    return render(request, 'Blog_GeneralindexG.html', {'posts': posts, 'pagina_actual': pagina_actual, 'paginas': paginas})

def NewPostG(request):
    form = AuthenticationForm() 
    return render(request, 'makeanewpostG.html', {'form': form})

def NewPostSaveG(request):
    if request.method == 'POST':
        print("POST")
     #Obteniendo datos del registro (Form)
        nombre = request.POST['nombre']
        anodecreacion = request.POST['anodecreacion']
        desarrollador = request.POST['desarrollador']
        user = User.objects.get(id=request.user.id)
        genero = request.POST['genero']
        plataforma = request.POST['plataforma']
        descripcion = request.POST['descripcion']
        contenido = request.POST['contenido']
        urlimagen = request.POST['urlimagen']

        #Guardando los datos en la DB
        publicacion = Juegos(nombre=nombre, anodecreacion=anodecreacion, desarrollador=desarrollador, user=user, genero=genero,plataforma=plataforma,descripcion=descripcion,urlimagen=urlimagen,contenido=contenido)
        publicacion.save()
        posteos = Publicacion.objects.filter(muestra_inferior='si')

    return render(request, 'indexBase.html',{'posteos':posteos})


def eliminarPostG(request, pk):
    
    if request.method == 'POST':
    
        post = get_object_or_404(Juegos, id=pk)
       
        if request.user == post.user:
            post.delete()
            print(pk)
            return render(request,'Blog_GeneralindexG.html')
        else:
            
            return render(request,'Blog_GeneralindexG.html')
    else:
        return render(request,'Blog_GeneralindexG.html')
    

def editPostG(request, id):

    post = Juegos.objects.get(id=id)
    
    if request.method == 'POST':
        
        miPost = CreaJuegos(request.POST)
    
        if miPost.is_valid():

            post.nombre = miPost.cleaned_data['nombre']
            post.anodecreacion = miPost.cleaned_data['anodecreacion']
            post.genero = miPost.cleaned_data['genero']
            post.plataforma = miPost.cleaned_data['plataforma']
            post.urlimagen = miPost.cleaned_data['urlimagen']
            post.descripcion = miPost.cleaned_data['descripcion']
            post.contenido = miPost.cleaned_data['contenido']
            post.save()
            print("guardado")
            return HttpResponseRedirect(reverse('DetalleJuego', args=[str(post.id)]))
    else:

        miPost = CreaJuegos(initial={'nombre': post.nombre, 'anodecreacion': post.anodecreacion, 'genero': post.genero, 'plataforma': post.plataforma, 'urlimagen':post.urlimagen, 'descripcion':post.descripcion, 'contenido':post.contenido})        
        return render(request,'editarPosteoG.html', {'miPost': miPost, 'juegos_id': id, 'nombre': post.nombre})


def darLikes(request, pk):
    if request.user.is_authenticated:
        post = Juegos.objects.get(id=pk)
        post.likes.add(request.user)
        post.save()
        
    return HttpResponseRedirect(reverse('DetalleJuego', args=[str(pk)]))


class JuegosUpdate(UpdateView):
    model = Juegos
    template_name = "edita-juego.html"
    fields = ('__all__')
    success_url = "/juegos/"

class Juegosdelete(DeleteView):
    model = Juegos
    template_name = "eliminar-juego.html"
    success_url = "/juegos/"

def buscar(request): 

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        juegos = Juegos.objects.filter(nombre__icontains=nombre)

        return render (request, "resultadoBusqueda.html", {"juegos": juegos, "nombre": nombre})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)


