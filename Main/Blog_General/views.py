from enum import auto
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
        
    return render(request, 'indexBase.html',)

 
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

    post = get_object_or_404(Publicacion, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('verpost', args=[str(pk)]))


def eliminarPost(request, pk):
    
    if request.method == 'POST':
    
        post = get_object_or_404(Publicacion, id=pk)
       
        if request.user == post.user:
            post.delete()
            print(pk)
            return render(request,'Blog_Generalindex.html')
        else:
            print("No autorizado")
            return render(request,'Blog_Generalindex.html')
    else:
        return render(request,'Blog_Generalindex.html')
    
   