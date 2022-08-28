from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models

from RegistroUsuarios.models import Avatar

from Main.settings import MEDIA_URL

import os
# Create your models here.

# Clase publicacion para guardar todos los posteos.
class Publicacion(models.Model):
    #Establecemos las opciones para muestra superior y muestra inferior (los admins podran determinar como se muestran los Post.)
    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('no', 'no'),
        ('si', 'si'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length = 200, default="Some String")
    contenido = RichTextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')
    likes = models.ManyToManyField(User, related_name='entry_likes', blank=True)
    avatar = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # El autor sera una ForeignKey la cual es igual al usuario conectado.

    def get_pk(self):
        
        return self.pk


    def AvatarPublicacion(self): #Buscamos el Avatar segun usuario/autor.
        if self.user:
            return Avatar.objects.filter(user=self.user.id).last().imagen.url if Avatar.objects.filter(user=self.user.id).last() else Avatar(user=self.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg')).imagen.url
        else:
            return Avatar(user=self.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg')).imagen.url

    def imagen_Publicacion(self): #Buscamos el Avatar segun usuario/autor.
        
        return BlogImagen.objects.filter(publicacion_id=self.id).last().imagen.url if BlogImagen.objects.filter(publicacion_id=self.id).last() else BlogImagen(publicacion_id=self.id, imagen=os.path.join(MEDIA_URL, 'img/defaultblog.jpg')).imagen.url
        


    def __str__(self):
        return self.titulo + " - "+ str(self.fecha)


    def total_likes(self): #Contador de Likes
        return self.likes.count()


    @property
    def number_of_comments(self):
        return Comentario.objects.filter(blogpost_connected=self).count()

# Class comentario , almacenamos los comentarios y los clasificamos por usuario ForeignKey Blogpost_Connected / user.
class Comentario(models.Model):
    blogpost_connected = models.ForeignKey(Publicacion, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def imagenComentario(self): #Buscamos el Avatar segun usuario/autor.
        if self.user:
            return Avatar.objects.filter(user=self.user.id).last().imagen.url if Avatar.objects.filter(user=self.user.id).last() else Avatar(user=self.user, imagen=os.path.join(MEDIA_URL, 'img/default.jpg')).imagen.url
        else:
            return None
    
    def __str__(self):
        return '%s - %s' % (self.user, self.body)  

class BlogImagen(models.Model):

    publicacion_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True ,blank=True, related_name="imagen_blog")
    imagen = models.ImageField(upload_to='BlogImagenes', blank=True , null=True)

    