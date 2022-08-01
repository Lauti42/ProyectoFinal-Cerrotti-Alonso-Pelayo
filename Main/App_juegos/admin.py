from django.contrib import admin
from App_juegos.models import Juegos , Desarrollador, Genero, Plataformas
# Register your models here.

admin.site.register(Juegos)
admin.site.register(Desarrollador)
admin.site.register(Genero)
admin.site.register(Plataformas)
