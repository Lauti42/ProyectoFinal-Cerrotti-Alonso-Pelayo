from enum import auto
from mimetypes import init
import re
from django.shortcuts import render, get_object_or_404, redirect
from Blog_General.models import Publicacion, Comentario
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .forms import NewCommentForm
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Avatar
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Blog_General.models import Publicacion
from Blog_General.forms import PublicacionForm
# Create your views here.


class PostDetalle(DetailView):
    model = Publicacion 
    context_object_name = 'post'
    template_name = 'GeneralPost.html'
    

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comentario.objects.filter(blogpost_connected= self.get_object()).order_by('-date_added')
        data['comments']= comments_connected
        stuff= get_object_or_404(Publicacion, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        data['total_likes']= total_likes

        if self.request.user.is_authenticated:
            data['comment_form']= NewCommentForm(instance=self.request.user)
            
        return data

    def post(self, request, *args, **kwargs):
        new_comment= Comentario(body= request.POST.get('body'), 
            user= self.request.user,
            blogpost_connected= self.get_object())
        
        new_comment.save()
        return self.get(self, request, *args, **kwargs)



def NewPostSave(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            print("POST")
        #Obteniendo datos del registro (Form)
            titulo = request.POST['titulo']
            contenido = request.POST['contenido']
            imagen = request.POST['imagen']
            user = User.objects.get(id=request.user.id)
            descripcion = request.POST['descripcion']
            
            #Guardando los datos en la DB
            publicacion = Publicacion(titulo=titulo, contenido=contenido, imagen=imagen, user=user, descripcion=descripcion)
            publicacion.save()
            posteos = Publicacion.objects.filter(muestra_inferior="si")
    return render(request, 'indexBase.html',{'posteos':posteos})

@login_required
def NewPost(request):
    
    form = AuthenticationForm() 
    return render(request, 'makeanewpost.html', {'form': form})


def blog_general_index(request):

    listado_posts= Publicacion.objects.all().order_by('-id')
    paginator= Paginator(listado_posts, 6)
    pagina= request.GET.get('page') or 1
    posts= paginator.get_page(pagina)
    pagina_actual= int(pagina)
    paginas= range(1, posts.paginator.num_pages + 1)


    
    return render(request, 'Blog_Generalindex.html', {'posts': posts, 'pagina_actual': pagina_actual, 'paginas': paginas})

def verpost(request):
    print(request)
    
    return render(request, 'indexBase.html')


def darLike(request, pk):
    if request.user.is_authenticated:
        post = Publicacion.objects.get(id=pk)
        post.likes.add(request.user)
        post.save()
        
    return HttpResponseRedirect(reverse('verpost', args=[str(pk)]))


def eliminarPost(request, pk):
    
    if request.method == 'POST':
    
        post = get_object_or_404(Publicacion, id=pk)
       
        if request.user == post.user:
            post.delete()
            return HttpResponseRedirect(reverse('blog_general_index'))
        else:
            return render(request,'Blog_Generalindex.html')
    else:
        
        return render(request,'Blog_Generalindex.html')
    


def editPost(request, id):

    post = Publicacion.objects.get(id=id)
    
    if request.method == 'POST':
        
        miPost = PublicacionForm(request.POST)
    
        if miPost.is_valid():

            post.titulo = miPost.cleaned_data['titulo']
            post.contenido = miPost.cleaned_data['contenido']
            post.imagen = miPost.cleaned_data['imagen']
            post.descripcion = miPost.cleaned_data['descripcion']
            post.save()
            return HttpResponseRedirect(reverse('verpost', args=[str(post.id)]))
    else:

        miPost = PublicacionForm(initial={'titulo': post.titulo, 'contenido': post.contenido, 'imagen': post.imagen, 'descripcion': post.descripcion})        
        return render(request,'editarPosteo.html', {'miPost': miPost, 'post_id': id, 'titulo': post.titulo})

def buscarPost(request):
    if request.GET["titulo"]:

        titulo = request.GET["titulo"]
        if titulo != None:
            publicacionBody = Publicacion.objects.filter(contenido__contains=titulo)
            rango = len(publicacionBody)
            print(rango)
            
            if len(publicacionBody) == 0:
                ceroData = "No se obtuvieron reusultados"
                return HttpResponseRedirect(reverse('blog_general_index'))
            else:
                return render(request, 'Blog_Generalindex.html', {'buesqueda_posteos': publicacionBody})
        else:
            return HttpResponseRedirect(reverse('blog_general_index'))

    else:
        return HttpResponseRedirect(reverse('blog_general_index'))
