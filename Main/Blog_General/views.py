from enum import auto
from django.shortcuts import render
from Blog_General.models import Entry
# Create your views here.


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

    post= Entry.objects.filter(muestra_inferior= 'si')

    return render(self, 'Blog_Generalindex.html', {'post': post})
