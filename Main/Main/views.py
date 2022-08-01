from django.shortcuts import render
from django.http import HttpResponse
from Blog_General.models import Entry

def indexview(self):

    posteos = Entry.objects.filter(muestra_inferior= 'si')

    return render(self, 'indexBase.html', {'posteos': posteos} )

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')


    

        
        