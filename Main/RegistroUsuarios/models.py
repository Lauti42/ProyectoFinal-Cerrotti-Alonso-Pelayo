from venv import create
from django.db import models

# Create your models here.
class Registro_usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    create = models.DateField(auto_now_add=True)


class Preferencias_Usuario(models.Model):
    lenguaje = models.CharField(max_length=40)
    backOfront = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)