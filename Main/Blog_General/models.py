from ssl import Options
from django.db import models
from django.urls import reverse

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
    post = models.ForeignKey(Entry, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.nombre, self.name) 