from ssl import Options
from django.db import models

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
    contenido = models.TextField(max_length=1000)
    imagen = models.URLField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')

    def __str__(self):
        return self.nombre + " - " + self.autor + " - " + str(self.fecha)