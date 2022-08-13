from enum import auto
from django.shortcuts import render
from Blog_General.models import Entry
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
# Create your views here.


class PostDetalle(DetailView):
    model = Entry
    context_object_name = 'post'
    template_name = 'GeneralPost.html'


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
    paginator= Paginator(listado_posts, 3)
    pagina= request.GET.get('page') or 1
    posts= paginator.get_page(pagina)
    current_page= range(1, posts.paginator.num_pages + 1)

    
   

    return render(request, 'Blog_Generalindex.html', {'posts': posts})

def verpost(request):
    print(request)
    return render(request, 'indexBase.html')


