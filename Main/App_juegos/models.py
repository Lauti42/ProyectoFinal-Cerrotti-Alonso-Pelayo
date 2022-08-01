from django.db import models

# Create your models here.

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.pais}'

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Plataformas(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.link}'

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

    def __str__(self) -> str:
        return f'{self.nombre} ({self.anodecreacion}) - {self.genero} - {self.desarrollador} - {self.plataforma} - {self.urlimagen} - {self.descripcion}'
