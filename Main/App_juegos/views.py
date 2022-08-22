from django.shortcuts import render
from .models import Desarrollador, Genero, Juegos, Plataformas, ComentarioG 
from .forms import CreaJuegos, NewCommentFormG
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.http import HttpResponse
from RegistroUsuarios.models import Avatar
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
        # total_likes = stuff.total_likes()
        # data['total_likes']= total_likes

        if self.request.user.is_authenticated:
            data['comment_form']= NewCommentFormG(instance=self.request.user)
            
        return data

    def post(self, request, *args, **kwargs):
        new_comment= ComentarioG(body= request.POST.get('body'), 
            user= self.request.user,
            blogpost_connected= self.get_object())
        
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class JuegosCreate(LoginRequiredMixin, CreateView):
    model = Juegos
    form_class = CreaJuegos
    template_name = "crea-juego.html"
    success_url = "/juegos/"

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


def all_games(request):

    post= Juegos.objects.all()
    # post_sup= Entry.objects.filter(muestra_superior= 'si')
   
    
    return render(request, 'Blog_GeneralindexG.html', {'post': post})