from django.urls import path 

from .views import DesarrolladorCreate, DesarrolladorDetail, DesarrolladorList, DesarrolladorUpdate, Desarrolladordelete, GeneroCreate, GeneroDetail, GeneroList, GeneroUpdate, Generodelete, JuegosCreate, JuegosDetail, JuegosList, JuegosUpdate, Juegosdelete, PlataformasCreate, PlataformasDetail, PlataformasList, PlataformasUpdate, Plataformasdelete, buscar, buscardesarrollador, buscargenero, buscarplataforma, all_games

urlpatterns = [

    path('', JuegosList.as_view(), name='juegos'),
    path('detalle-juego/<pk>', JuegosDetail.as_view(), name= "DetalleJuego"),
    path('crea-juegos/', JuegosCreate.as_view(), name="CreaJuego"),
    path('edita-juego/<pk>', JuegosUpdate.as_view(), name="EditaJuego"),
    path('eliminar-juegos/<pk>', Juegosdelete.as_view(), name="EliminarJuego"),
    path('buscar-juego', buscar, name="Buscar"),
    path('todos-los-juegos', all_games, name="all_games"),

    path('generos/', GeneroList.as_view(), name= "ListaGenero"),
    path('detalle-genero/<pk>', GeneroDetail.as_view(), name= "DetalleGenero"),
    path('crea-genero/', GeneroCreate.as_view(), name="CreaGenero"),
    path('edita-genero/<pk>', GeneroUpdate.as_view(), name="EditaGenero"),
    path('eliminar-genero/<pk>', Generodelete.as_view(), name="EliminarGenero"),
    path('buscar-genero', buscargenero, name="BuscarGenero"),

    path('desarrolladores/', DesarrolladorList.as_view(), name= "ListaDesarrollador"),
    path('detalle-desarrollador/<pk>', DesarrolladorDetail.as_view(), name= "DetalleDesarrollador"),
    path('crea-desarrollador/', DesarrolladorCreate.as_view(), name="CreaDesarrollador"),
    path('edita-desarrollador/<pk>', DesarrolladorUpdate.as_view(), name="EditaDesarrollador"),
    path('eliminar-desarrollador/<pk>', Desarrolladordelete.as_view(), name="EliminarDesarrollador"),
    path('buscar-desarrollador', buscardesarrollador, name="BuscarDesarrollador"),

    path('plataformas/', PlataformasList.as_view(), name= "ListaPlataforma"),
    path('detalle-plataforma/<pk>', PlataformasDetail.as_view(), name= "DetallePlataforma"),
    path('crea-plataforma/', PlataformasCreate.as_view(), name="CreaPlataforma"),
    path('edita-plataforma/<pk>', PlataformasUpdate.as_view(), name="EditaPlataforma"),
    path('eliminar-plataforma/<pk>', Plataformasdelete.as_view(), name="EliminarPlataforma"),
    path('buscar-plataforma', buscarplataforma, name="BuscarPlataforma"),


 
]
