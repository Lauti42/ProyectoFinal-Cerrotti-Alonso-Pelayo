from django.db import models
from RegistroUsuarios.models import Avatar
from django.contrib.auth.models import User

# Create your models here.

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Plataformas(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Juegos(models.Model):

    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('si', 'Si'),
        ('no', 'No'),
    )


    nombre = models.CharField(max_length=50)
    anodecreacion = models.IntegerField()
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataformas, on_delete=models.CASCADE)
    urlimagen = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')
    avatar = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    def AvatarJuegos(self):
        if self.user:
            return Avatar.objects.filter(user=self.user.id).last().imagen.url if Avatar.objects.filter(user=self.user.id).last() else None
        else:
            return None

    def __str__(self) -> str:
        return f'{self.nombre} ({self.anodecreacion})'
    
   
class ComentarioG(models.Model):
    blogpost_connected = models.ForeignKey(Juegos, related_name="comments", on_delete=models.CASCADE)
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
