from enum import auto
from django.shortcuts import render
from Blog_General.models import Entry
from django.views.generic.detail import DetailView
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
        
        #Guardando los datos en la DB
        Entrys = Entry(nombre=nombre, contenido=contenido, imagen=imagen, autor=autor)
        Entrys.save()
        
    return render(request, 'indexBase.html')


def NewPost(request):
    return render(request, 'makeanewpost.html')


def blog_general_index(self):

    post= Entry.objects.all()
    # post_sup= Entry.objects.filter(muestra_superior= 'si')
   

    return render(self, 'Blog_Generalindex.html', {'post': post})

def verpost(request):
    print(request)
    return render(request, 'indexBase.html')


