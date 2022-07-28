from django.db import models

# Create your models here.

class Entry(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField(max_length=1000)
    imagen = models.URLField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre + " - " + self.autor + " - " + str(self.fecha) + " - " + self.contenido[:100] + "..." +  " - " + self.imagen + " - "