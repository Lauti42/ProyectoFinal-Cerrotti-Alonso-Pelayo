
from venv import create
from django.db import models

# Create your models here.
class Registro_usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre + " " + self.email


class Preferencias_Usuario(models.Model):
    lenguaje = models.CharField(max_length=40)
    backOfront = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)

    def __str__(self):
        return self.lenguaje + " " + self.backOfront + " " + self.pais + " " + self.trabajo

    class Meta():
        verbose_name = "Preferencias"
        
