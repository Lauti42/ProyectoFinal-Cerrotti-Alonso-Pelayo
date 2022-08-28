# @staff_member_required
# def editPostAdmin(request, id): # Editar Posteo.

#     post = Publicacion.objects.get(id=id) #Obtenemos el objeto segun id
    
#     if request.method == 'POST':  #Si el method es POST remplazaremos los campos del Form por los ingresados en la Request
        
#         miPost = PublicacionForm(request.POST)
        
#         if miPost.is_valid():

#             post.__dict__.update(miPost.cleaned_data)
#             post.save()
#             return HttpResponseRedirect(reverse('verpost', args=[str(post.id)])) 
#         else:
#             context = miPost.errors# Volvemos al blog editado
#             return render(request,'editarPosteoAdmin.html', {'miPost': miPost, 'post_id': id, 'titulo': post.titulo,'errors':context})
#     else: # De lo contrario pasamos los formularios correspondientes a editarPosteo.

#         miPost = PublicacionForm(initial={'titulo': post.titulo, 'contenido': post.contenido, 'imagen': post.imagen, 'descripcion': post.descripcion})        
#         return render(request,'editarPosteoAdmin.html', {'miPost': miPost, 'post_id': id, 'titulo': post.titulo})
