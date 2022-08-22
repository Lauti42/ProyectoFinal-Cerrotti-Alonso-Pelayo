from django.urls import path 

from .views import DesarrolladorCreate, DesarrolladorDetail, DesarrolladorUpdate, Desarrolladordelete, NewPostG, GeneroDetail, GeneroUpdate, Generodelete,GeneroCreate, JuegosDetail, JuegosUpdate, Juegosdelete, PlataformasCreate, PlataformasDetail, PlataformasUpdate, Plataformasdelete, buscar, buscardesarrollador, buscargenero, buscarplataforma,NewPostSaveG,blog_general_indexG,darLikes,editPostG,eliminarPostG

urlpatterns = [

    path('', blog_general_indexG, name='juegos'), #Renderiza el index de Blogs Games (Terminado)
    path('detalle-juego/<pk>', JuegosDetail.as_view(), name="DetalleJuego"), # Muestra cada post Games individualmente (Terminado)
    path('crea-juegos/', NewPostG, name="NewPostG"), # Formulario para subir un nuevo PostGames (Terminado)
    path('edita-juego/<id>', editPostG, name="editPostG"),
    path('eliminar-juegos/<pk>', eliminarPostG, name="eliminarPostG"), # Eliminar posteo
    path('buscar-juego', buscar, name="Buscar"),
    path('likes/<int:pk>', darLikes, name='likes_posts'),
    path('juego_guardado' , NewPostSaveG, name="NewPostSaveG"), # Guarda el formulario de los posteos PostGames dentro del modelo. (Terminado)

    path('detalle-genero/<pk>', GeneroDetail.as_view(), name= "DetalleGenero"),
    path('crea-genero/', GeneroCreate.as_view(), name="CreaGenero"),
    path('edita-genero/<pk>', GeneroUpdate.as_view(), name="EditaGenero"),
    path('eliminar-genero/<pk>', Generodelete.as_view(), name="EliminarGenero"),
    path('buscar-genero', buscargenero, name="BuscarGenero"),


    path('detalle-desarrollador/<pk>', DesarrolladorDetail.as_view(), name= "DetalleDesarrollador"),
    path('crea-desarrollador/', DesarrolladorCreate.as_view(), name="CreaDesarrollador"),
    path('edita-desarrollador/<pk>', DesarrolladorUpdate.as_view(), name="EditaDesarrollador"),
    path('eliminar-desarrollador/<pk>', Desarrolladordelete.as_view(), name="EliminarDesarrollador"),
    path('buscar-desarrollador', buscardesarrollador, name="BuscarDesarrollador"),


    path('detalle-plataforma/<pk>', PlataformasDetail.as_view(), name= "DetallePlataforma"),
    path('crea-plataforma/', PlataformasCreate.as_view(), name="CreaPlataforma"),
    path('edita-plataforma/<pk>', PlataformasUpdate.as_view(), name="EditaPlataforma"),
    path('eliminar-plataforma/<pk>', Plataformasdelete.as_view(), name="EliminarPlataforma"),
    path('buscar-plataforma', buscarplataforma, name="BuscarPlataforma"),


 
]
