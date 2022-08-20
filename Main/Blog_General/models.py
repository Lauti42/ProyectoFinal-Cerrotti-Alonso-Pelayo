from email.mime import image
from ssl import Options
from django.db import models
from django.urls import reverse
from RegistroUsuarios.models import Avatar
from django.contrib.auth.models import User
# Create your models here.


class Publicacion(models.Model):

    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('si', 'Si'),
        ('no', 'No'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length = 200, default="Some String")
    contenido = models.TextField(max_length=3500)
    imagen = models.URLField(max_length=3000, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')
    likes = models.ManyToManyField(User, related_name='entry_likes')
    avatar = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    def AvatarPublicacion(self):
        if self.user:
            return Avatar.objects.filter(user=self.user.id).last().imagen.url if Avatar.objects.filter(user=self.user.id).last() else None
        else:
            return None


    def __str__(self):
        return self.titulo + " - "+ str(self.fecha)


    def total_likes(self):
        return self.likes.count()


    @property
    def number_of_comments(self):
        return Comentario.objects.filter(blogpost_connected=self).count()


class Comentario(models.Model):
    blogpost_connected = models.ForeignKey(Publicacion, related_name="comments", on_delete=models.CASCADE)
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