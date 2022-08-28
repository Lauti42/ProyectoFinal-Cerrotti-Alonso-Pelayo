# def editPost(request, id): # Editar Posteo.

#     post = Publicacion.objects.get(id=id) #Obtenemos el objeto segun id
    
#     if request.method == 'POST':  #Si el method es POST remplazaremos los campos del Objet por los ingresados en la Request
        
#         miPost = PublicacionForm(request.POST)
        
#         if miPost.is_valid():

#             post.__dict__.update(miPost.cleaned_data)
#             post.save()
            
 
#             if ImgForm.is_valid():
#                 ImagenPost = ImgForm.cleaned_data
#                 print(ImagenPost)
#                 if ImagenPost['imagen'] == None and BlogImagen.objects.filter(publicacion_id=post).last():
#                     print("1")
#                     imagenB = BlogImagen.objects.filter(publicacion_id=post).last()
#                     imagenB.save()
#                 elif ImagenPost['imagen'] == None and BlogImagen.objects.filter(publicacion_id=post.id).last() == None:
#                     print("2")
#                     imagenB = BlogImagen(publicacion_id=post, imagen=os.path.join(MEDIA_URL, 'img/defaultblog.jpg'))
#                     imagenB.save()
#                 elif ImagenPost['imagen'] != None:
#                     print("3")
#                     print(ImagenPost["imagen"])
#                     imagenB = BlogImagen(publicacion_id=post, imagen=ImagenPost["imagen"])
#                     imagenB.save()

#             return render(request, "indexBase.html", {"mensaje": "Datos Actualizados tu publicacion se encuentra en etapa de revision."})
#         else:
#             context = miPost.errors# Volvemos al blog editado
#             return render(request,'editarPosteoAdmin.html', {'miPost': miPost, 'post_id': id, 'titulo': post.titulo,'errors':context})   
#     else: # De lo contrario pasamos los formularios correspondientes a editarPosteo.

#         miPost = PublicacionFormAdmin(initial={'titulo': post.titulo, 'contenido': post.contenido, 'imagen': post.imagen, 'descripcion': post.descripcion})        
#         ImgForm = BlogImagenForm()
#         return render(request,'editarPosteoAdmin.html', {'miPost': miPost, 'post_id': id, 'titulo': post.titulo,'ImgForm':ImgForm})