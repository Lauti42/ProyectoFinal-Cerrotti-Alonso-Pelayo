
from django.shortcuts import render
from django.views.generic import TemplateView

from Blog_General.models import Publicacion


def indexview(request): #Renderizamos IndexBase con los posteos que tengan la propiedad Muestra_Inferior="si"

    posteos = Publicacion.objects.filter(muestra_inferior= 'si')
    return render(request, 'indexBase.html', {'posteos': posteos})

class Error404View(TemplateView): # Creamos un template que se renderizara en caso de que la url no corresponda.
    template_name = "error_404.html"

def aboutview(request): # Vista de About about.html
    return render(request, 'about.html') 

def contactview(request): # Vista de contactos contact.html
    return render(request, 'contact.html')



        
        