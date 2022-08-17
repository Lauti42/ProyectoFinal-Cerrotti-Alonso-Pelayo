from email.mime import image
from ssl import Options
from django.db import models
from django.urls import reverse
from RegistroUsuarios.models import Avatar
from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):

    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('si', 'Si'),
        ('no', 'No'),
    )



    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length = 150, default="Some String")
    contenido = models.TextField(max_length=1000)
    imagen = models.URLField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')


    def __str__(self):
        return self.nombre + " - " + self.autor + " - " + str(self.fecha)


class Comentario(models.Model):
    blogpost_connected = models.ForeignKey(Entry, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def imagenComentario(self):
        if self.user:
            return Avatar.objects.filter(user=self.user.id).last().imagen.url if Avatar.objects.filter(user=self.user.id).last() else None
        else:
            return None
    
    def __str__(self):
        return '%s - %s' % (self.user, self.body)  