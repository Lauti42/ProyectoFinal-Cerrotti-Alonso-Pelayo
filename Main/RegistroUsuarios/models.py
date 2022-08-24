

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#Class Avatar , contiene una imagen y un usuario como referencia.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)

    def __str__(self):
        return self.user.username