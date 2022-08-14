from enum import auto
from django.shortcuts import render
from Blog_General.models import Entry, Comentario
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .forms import NewCommentForm
# Create your views here.


class PostDetalle(DetailView):
    model = Entry
    context_object_name = 'post'
    template_name = 'GeneralPost.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comentario.objects.filter(blogpost_connected= self.get_object()).order_by('-date_added')
        data['comments']= comments_connected
        if self.request.user.is_authenticated:
            data['comment_form']= NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment= Comentario(body= request.POST.get('body'), 
            name= self.request.user,
            blogpost_connected= self.get_object())
        
        new_comment.save()
        return self.get(self, request, *args, **kwargs)



def NewPostSave(request):
    if request.method == 'POST':
        print("POST")
     #Obteniendo datos del registro (Form)
        nombre = request.POST['nombre']
        contenido = request.POST['contenido']
        imagen = request.POST['imagen']
        autor = request.POST['autor']
        descripcion = request.POST['descripcion']
        
        #Guardando los datos en la DB
        Entrys = Entry(nombre=nombre, contenido=contenido, imagen=imagen, autor=autor, descripcion=descripcion)
        Entrys.save()
        
    return render(request, 'indexBase.html')


def NewPost(request):
    return render(request, 'makeanewpost.html')


def blog_general_index(request):

    listado_posts= Entry.objects.all().order_by('-id')
    paginator= Paginator(listado_posts, 2)
    pagina= request.GET.get('page') or 1
    posts= paginator.get_page(pagina)
    pagina_actual= int(pagina)
    paginas= range(1, posts.paginator.num_pages + 1)

    
   

    return render(request, 'Blog_Generalindex.html', {'posts': posts, 'pagina_actual': pagina_actual, 'paginas': paginas})

def verpost(request):
    print(request)
    return render(request, 'indexBase.html')


