from django.shortcuts import render
from django.http import HttpResponse



def aboutview(request):
    return render(request, 'about.html')

def contactview(request):
    return render(request, 'contact.html')


    

        
        