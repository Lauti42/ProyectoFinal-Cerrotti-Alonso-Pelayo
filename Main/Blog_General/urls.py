"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Blog_General.views import (NewPost, NewPostSave, PostDetalle,
                                blog_general_index, darLike, editPost,
                                eliminarPost, adminPosts)

from .views import  buscarPost, darLike

urlpatterns = [
    path('General/index/', blog_general_index , name='blog_general_index'),
    path('General/NewPost/', NewPost, name='NewPost'),
    path('General/NewPost/save', NewPostSave, name='NewPostSave'),
    path('General/VerPost/<int:pk>', PostDetalle.as_view(), name='verpost'),
    path('like/<int:pk>', darLike, name='like_post'),
    path('eliminarPost/<int:pk>', eliminarPost, name='eliminarPost'),
    path('editarPost/<int:id>', editPost, name='editPost'),
    path('buscar/blogs/', buscarPost, name='buscarPost'),
    path('administrar/drafts', adminPosts, name='adminPosts'),
    
    
    
]
     