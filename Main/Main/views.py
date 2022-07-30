from django.shortcuts import render
from django.http import HttpResponse

def indexview(request):
    return render(request, 'indexBase.html')

def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')


    

        
        