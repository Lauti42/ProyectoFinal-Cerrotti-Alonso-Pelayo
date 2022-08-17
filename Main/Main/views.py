from django.shortcuts import render
from django.http import HttpResponse
from Blog_General.models import Entry
from RegistroUsuarios.views import login_request
from django.contrib.auth.forms import AuthenticationForm
from RegistroUsuarios.models import Avatar

def indexview(request):

    posteos = Entry.objects.filter(muestra_inferior= 'si')
    return render(request, 'indexBase.html', {'posteos': posteos})

def aboutview(request):
    return render(request, 'about.html') 

def contactview(request):
    
    
    return render(request, 'contact.html')



        
        