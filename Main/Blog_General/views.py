from enum import auto
from django.shortcuts import render
from Blog_General.models import Entry
# Create your views here.

def blog_general_index(request):
    
    return render(request, 'Blog_Generalindex.html')

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

    return render(request, 'Blog_Generalindex.html')

def NewPost(request):
    return render(request, 'makeanewpost.html')


def GeneralPost(request):

    nombre= None
    contenido= None
    imagen= None
    autor=  None
    fecha=  None

    for entry in Entry.objects.all()
        for post in entry:
            nombre= post.nombre
            contenido= post.contenido
            imagen= post.imagen
            autor= post.autor
            fecha= post.fecha

    
    # entries = Entry.objects.all()
    # for entry in entries:
    #     nombre = entry.nombre
    #     contenido = entry.contenido
    #     imagen = entry.imagen
    #     autor = entry.autor
    #     fecha = entry.fecha
        
    return render(request, "Blog_Generalindex.html", {'entries': entries, 'nombre': nombre, 'contenido': contenido, 'imagen': imagen, 'autor': autor, 'fecha': fecha})
    #return render(request, "Blog_Generalindex.html", {'entries': entries, 'nombre': nombre, 'contenido': contenido, 'imagen': imagen, 'autor': autor, 'fecha': fecha})