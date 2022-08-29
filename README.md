<em>Entrega1-   Cerrotti  Pelayo   Alonso </em>

<h1 aling="center" >Primera entrega del Proyecto Final.</em>

### Indice:

:page_facing_up:Templates:
* Inicio.
* Registro
* About
* Blog Index
* Blog Search
* Blog Post
* Editar Post
* Blog View
* Modificar Perfil
* Administrador


:wrench:Modelos:

* Modelo de Blog_General (app)
* Modelo de Registro_Usuarios (app)


:spiral_notepad:Formularios: 
* Formularios de Blog_General (app)
* Formularios de Registro_Usuarios (app)

:hammer:Funcionalidades del proyecto
* :hammer:Registrar usuarios.
* :hammer:LogIn de usuarios.  
* :hammer:Realizar Posteos. 
* :hammer:Editar Posteos.
* :hammer:Eliminar Posteos.
* :hammer:Administrar Posteos.
* :hammer:Dar Like, Comentar.
* :hammer:Modificar perfil completo.
* :hammer:Ver todos los posteos, buscar posteos.


:abc:Orden de Prueba:
* Registro
* Blog 
* Administrador

:abc:Usuarios con permisos de Staff:
	Lalonso
   lcerrotti
   Lauri
   LioMessi : Qatar2022

:hammer_and_wrench:Futuros Cambios:

<br></br>
<h2 aling="center" >Templates</h2>


1) Templates / Inicio: 
   
   [![Index-Nuevo.png](https://i.postimg.cc/YCYRV2dy/Blog-LLL-Index.png)](https://postimg.cc/GHb07WtQ)
   
   * En el index podemos encontrar un encabezado donde nos da la Bienvenida
   * Podemos encontrar una barra de navegacion que nos guiara a cada una de nuestras funcionalidades.
   * En la parte inferior de el Index se muestran los blogs que nosotros elegimos para mostrar (mas informacion en Models)
   * Dentro del encabezado existen 2 botones que nos redirigen al formulario de Registro y al About.
   
    Proximo a implementar:
   * Construir la funcionalidad para que el usuario coloque su email para que nosotros podamos contactarlo.
   <br></br>
   
2) Templates / Registro:
    
    [![Registro-Primer-formulario.png](https://i.postimg.cc/HWNtk8Kh/Blog-LLL-Registro.png)](https://postimg.cc/p95XWwDj)
    
    * El template de Registro , es una extencion del Index , se agrega unicamente Un formulario y una generalizacion de las actividades que se pueden realizar.
    <br></br>
    
    
3) Templates / About:
    
      [![Registro-Primer-formulario.png](https://i.postimg.cc/633d9BhK/Sobre-Nosotros.png)](https://postimg.cc/p95XWwDj)
    
    * Es un template individual , contiene una descripcion individual de cada uno de los integrantes
    * Al final del template se puede econtrar una seccion donde Estan los integrantes.
    <br></br>
    
4) Templates / Blog Index: 
    
    [![Blog-Index-Nuevo.png](https://i.postimg.cc/3wZB8S5X/Blog-Entradas.png)](https://postimg.cc/CRTsF0Ty)
    
    * Blog Index es un template Individual , contiene una navbar propia.
    * El proposito de Blog Index es resaltar un Blog de nuestra eleccion  (Mas informacion en Models) y mostrar todos los blogs creados por los usuarios.
    <br></br>
 
5) Templates / Blog Search: 
    
    [![Blog-Index-Nuevo.png](https://i.postimg.cc/Zn5DzkWv/Blog-Entradas-Search.png)](https://postimg.cc/CRTsF0Ty)
    
    * Funcionalidad implementada en BlogIndex
    * Caja de busqueda, filtra lo ingresado en el campo por todo el cuerpo de las publicaciones existentes y renderiza el resultado..
    <br></br> 


6) Templates / Blog Post: 
    
    [![Blog-Post.png](https://i.postimg.cc/N08NyGTr/Blog-LLL-Posteos.png)](https://postimg.cc/yJrJ8hgJ)
    
    * Blog Post es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede agregar un autor , contenido , imagen , asunto y descripcion.
    <br></br>
    
    
7) Templates / Editar Post:
    
    [![Blog-Publicado.png](https://i.postimg.cc/Dfpx4MW5/Blog-LLL-Editar.png)](https://postimg.cc/XZhJbVmd)
    
    * Es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede editar contenido , imagen , asunto y descripcion.
    <br></br>
    
    
8) Templates / Blog View:
    
    [![Blog-Publicado.png](https://i.postimg.cc/GpbF5F8H/Entrada-1.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Publicacion 
    * Renderiza Autor,Contenido,Imagen, Avatar, Comentarios , Likes, asunto.
    <br></br>
    
    
9) Templates / Modificar Perfil:
    
    [![Blog-Publicado.png](https://i.postimg.cc/j21vVDVB/Blog-LLL-Modificar-Perfil.png)](https://postimg.cc/XZhJbVmd)
    
    * Es un template extendido del Index, solo se conserva la nabvar.
    * Renderiza un formulario de editar perfil junto a todos los posteos que ese usuario publico. 
    * Se puede modificar todos los campos, hasta su contraseña
    <br></br>
   
    
10) Templates / Administrador:
    
    [![Blog-Publicado.png](https://i.postimg.cc/d0cHtZ7Y/Blog-LLL-Administrador.png)](https://postimg.cc/XZhJbVmd)
    
    * Es un template extendido del Index, solo se conserva la nabvar.
    * Renderiza todos los objetos de Publicacion , permite al administrador , editar , publicar y eliminar los posteos de los usuarios comunes.
    
    <br></br>
  

    



<br></br>
<h2 aling="center" >Modelos</h2>

 
1) Modelos / Blog General (app).
   
   ```Python 
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
    contenido = models.TextField(max_length=3500)
    imagen = models.URLField(max_length=3000, blank=True, null=True)
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


    def __str__(self):
        return self.titulo + " - "+ str(self.fecha)


    def total_likes(self): #Contador de Likes
        return self.likes.count()


    @property
    def number_of_comments(self):
        return Comentario.objects.filter(blogpost_connected=self).count()

   #Class comentario , almacenamos los comentarios y los clasificamos por usuario ForeignKey Blogpost_Connected / user.
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
   ```
   * Class de Pulbicacion : La mayoria de las propiedades del objeto sirven para mosntrar el contenido en las paginas seleccionadas de la publicacion de un autor.
   Luego tiene varias propiedades que nos ayudan a determinar la ubicacion de la publicacion en el sitio , su estado de publicacion , likes y comentarios.
   
   * Class de Comentario: Utilizamos esta clase para vincular los comentarios con cada objeto de Publicacion.
     <br></br>
     
 2) Modelos / Registro_Usuarios (app):
      
    ```Python
    class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)

    def __str__(self):
        return self.user.username
    ```
    * Class Avatar: Utilizamos esta clase para vincular los avatars con cada usuario registrado. 
      <br></br>
 
 

<br></br>
<h2 aling="center" >Formularios</h2>


1) Formulario de Blog_General (app):
   
   ```Python
   class NewCommentForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ("body",)
        widgets= {
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Comenta aqui',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    
                }
            )
        }
        

   #Damos formato al form de PublicacionForm        
   class PublicacionForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(PublicacionForm, self).__init__(*args, **kwargs)
        self.fields['publicado'].required = False
        self.fields['muestra_superior'].required = False
        self.fields['muestra_inferior'].required = False 
        self.fields['likes'].required= False
        
        

    
    class Meta:
        model= Publicacion
        fields= ("titulo", "contenido", "imagen", "descripcion","publicado",'muestra_superior','muestra_inferior','likes')
        widgets= {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario un titulo para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            'contenido': forms.Textarea(
                attrs={
                    'placeholder': 'Es necesario un contenido para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:314px;',
                    
                }
            ),
            'imagen': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una imagen para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una descripcion para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:90px;',
                    
                }
            )
        }
   ```
  
   <br></br>
   
   
2) Formulario de Registro_Usuarios (app):
   
   ```Python
   username_validator = UnicodeUsernameValidator()

      # Formulario de Registro , establecemos los Placeholders, caracteres y formato

    class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label=_('.'),max_length=12, min_length=4, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}))
    last_name = forms.CharField(label=_('.'),max_length=12, min_length=4, required=True,
                               widget=(forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'})))
    email = forms.EmailField(label=_('.'),max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'})))
    password1 = forms.CharField(label=_('.'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña'})),
                                help_text=_('Al menos 8 caracteres alfanumericos'))
    password2 = forms.CharField(label=_('.'), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Repetir Contraseña'}),
                                help_text=_('Ingresa de nuevo tu contraseña para Confirmar'))
    username = forms.CharField(
        label=_('.'),
        max_length=150,
        help_text=_(''),
        validators=[username_validator],
        error_messages={'unique': _("El nombre de usuario ingresado ya existe")},
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Usuario'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        

      # Formulario de Edicion de perfil , establecemos los Placeholders, caracteres y formato
      class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','username']
        widgets= {
            'imagen': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'required': 'true',
                    'data-sb-validations':'required|email',
                    'data-sb-errors':'Email no válido',
                    'data-sb-required-message':'Email requerido',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Nombre requerido',
                    'data-sb-required-message':'Nombre requerido',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Apellido requerido',
                    'data-sb-required-message':'Apellido requerido',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Nombre de usuario',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Nombre de usuario requerido',
                    'data-sb-required-message':'Nombre de usuario requerido',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Contraseña requerida',
                    'data-sb-required-message':'Contraseña requerida',
                }
            ),
            
        }

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"] or password2.isnumeric() or len(password2) < 8:
            raise forms.ValidationError("...")
            
        return password2


      #Traemos el formulario de Avatar para renderizarlo con formato en la web.
      class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',) 
        widgets= {
            'imagen': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                
                }
            ),
        }
        class PublicacionFormAdmin(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(PublicacionFormAdmin, self).__init__(*args, **kwargs)
        self.fields['publicado'].required = False
        self.fields['muestra_superior'].required = False
        self.fields['muestra_inferior'].required = False 
        self.fields['likes'].required= False
        
        

    
    class Meta:
        model= Publicacion
        fields= ("titulo", "descripcion", "contenido", "imagen","publicado",'muestra_superior','muestra_inferior','likes')
        widgets= {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario un titulo para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            'contenido': forms.Textarea(
                attrs={
                    'placeholder': 'Es necesario un contenido para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:314px;',
                    
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una descripcion para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:90px;',
                    
                }
            ),
            'imagen': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una imagen para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            
        }        
     ```

   
<br></br>
<h2 aling="center" >Orden de Prueba</h2>

Para probar todo el contenido recomendamos una secuencia que lo llevara atravez de cada funcionalidad implementada al momento.

Registro/Login:

   * Iniciamos por index. Simplemente ingresando al link http://127.0.0.1:8000/ podemos visualizar el index completo
   * Seguimos por el registro, haciendo click en el boton Registrarte se cargara la vista registro y procederas a ingresar tus datos.
   * Dirigirse a la navbar y en el boton INICIAR se abrira un formulario de inicio.
   
Crear Posteo:   
   
   * Una vez conectado, podemos crear un post nosotros y para ello necesitamos ingresar a Blog/Blog Post en la navbar.
   * Aqui veremos un formulario donde llenaremos los datos del Posteo a realizar (en imagen utilizar una url)
   * Ya tenemos nuestro posteo creado pero para poder verlo publicado, primero un administrador debera autorizar la publicacion.

Administrador:
   
   * Si ingresamos con un usuario de staff , debajo de nuestro perfil aparece la opcion de Administrar, lo que nos llevara a el admin.
   * Dentro del admin podemos ver los posteos esperando autorizacion arriba y los ya publicados abajo.
   * Desde alli podremos editar, publicar o eliminar.
   * Si entramos a editar, tendremos campos que como usuarios comunes no teniamos.
   * Publicacion: Draft(no pulbicado) , Publicado (se publicara dentro del sitio)
   * muestra_superior: Mostramos la publicacion en la parte superior de Blog_General
   * muestra_inferior: Mostramos la publicacion en la parte inferior de IndexBase
   
Editar y modificar Publicaciones:
   
   * Desdde cualquier usuario, una vez creado una Publicacion, Podremos ver 2 botones (solo si la publicacion te pertenece)
   * El primer boton es el de eliminar, al hacer click sobre el nos saldra una advertencia que debemos aceptar para terminar de eliminar el Posteo
   * El segundo boton es el de editar, al hacer click nos llevara a un formulario donde podremos editar completamente el posteo.
   * Hay que tener en cuenta que al editar dicho posteo, debera pasar por la etapa de autorizacion (admin) otra vez antes de ser publicado.
  
  
<br></br>
<h2 aling="center" >Futuros cambios</h2>


* Establecer tamaños de imagenes estaticos para distintas partes de la web.
* Sistema de comunicacion via Email.

