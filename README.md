<em>Entrega1-   Cerrotti  Pelayo   Alonso </em>

<h1 aling="center" >Primera entrega del Proyecto Final.</em>

### Indice:

:page_facing_up:Templates:
* Inicio.
* Registro
* Registrado / Registrar Preferencias
* Preferencias Agregadas
* Buscar Preferencias
* Resutlados Preferencias
* About
* Blog Index
* Blog Post
* Blog View
* Blog Juegos

:wrench:Modelos:

* Modelo de Registro
* Modelo de Preferencias
* Modelo de Blog Entry
* Modelo de Juegos

:spiral_notepad:Formularios: 
* Formulario de Preferencias
* Modelo de Juegos
* Modelo de Desarrolladores
* Modelo de Generos
* Modelo de Plataformas

:hammer:Funcionalidades del proyecto
* :hammer:Registrar usuarios. Tenemos la funcionalidad de guardar datos que ingresan nuestros usuarios en la Base de datos.
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
* :hammer:Filtrar preferencias. Tenemos la funcionalidad de revisar las preferencias de nuestros usuarios.
* :hammer:Realizar Posteos. Tenemos la funcionalidad de realizar posteos, reflejarlos en la Base de datos y mostrarlos a eleccion dentro de todo el sitio.

:abc:Orden de Prueba:
* Registro / Preferencias / Busqueda / Blog**.
* **Blog / Blog Juegos / Formularios(Desarrolladores, Generos, Plataformas, Juegos) / Inicio / Busqueda

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
    
    * Blog Index es un template Individual , contiene una navbar propia.
    * El proposito de Blog Index es resaltar un Blog de nuestra eleccion  (Mas informacion en Models) y mostrar todos los blogs creados por los usuarios.
    <br></br> 


6) Templates / Blog Post: 
    
    [![Blog-Post.png](https://i.postimg.cc/N08NyGTr/Blog-LLL-Posteos.png)](https://postimg.cc/yJrJ8hgJ)
    
    * Blog Post es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede agregar un autor , contenido , imagen , asunto.
    <br></br>
    
    
7) Templates / Editar Post:
    
    [![Blog-Publicado.png](https://i.postimg.cc/Dfpx4MW5/Blog-LLL-Editar.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Publicacion 
    * Renderiza Autor,Contenido,Imagen, Avatar, Comentarios , Likes, asunto.
    <br></br>
    
    
8) Templates / Blog View:
    
    [![Blog-Publicado.png](https://i.postimg.cc/GpbF5F8H/Entrada-1.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Publicacion 
    * Renderiza Autor,Contenido,Imagen, Avatar, Comentarios , Likes, asunto.
    <br></br>
    
    
9) Templates / Modificar Perfil:
    
    [![Blog-Publicado.png](https://i.postimg.cc/j21vVDVB/Blog-LLL-Modificar-Perfil.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Publicacion 
    * Renderiza Autor,Contenido,Imagen, Avatar, Comentarios , Likes, asunto.
    <br></br>
   
    
10) Templates / Administrador:
    
    [![Blog-Publicado.png](https://i.postimg.cc/d0cHtZ7Y/Blog-LLL-Administrador.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Publicacion 
    * Renderiza Autor,Contenido,Imagen, Avatar, Comentarios , Likes, asunto.
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
   * Nombre - Email - Contraseña - Create (Determina automaticamente la fecha de creacion del registro.)
     <br></br>
     
 2) Modelos / Registro_Usuarios (app):
      
    ```Python
    class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)

    def __str__(self):
        return self.user.username
    ```
    * Lenguaje - Backend o Frontend - Pail - Trabajo. 
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
   * asdasdasdasdasd
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
     ```
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
   
<br></br>
<h2 aling="center" >Orden de Prueba</h2>

Para probar todo el contenido recomendamos una secuencia que lo llevara atravez de cada funcionalidad implementada al momento.

   * Iniciamos por index. Simplemente ingresando al link http://127.0.0.1:8000/ podemos visualizar el index completo
   * Seguimos por el registro, haciendo click en el boton Registrarte se cargara la vista registro y procederas a ingresar tus datos.
   * A continuacion , al enviar el formulario entraras a una web donde confirma tu registro. si bajas en la web tendras otro formulario para completar (Pref)
   * Si completaste todos los datos , pasaras a otra web donde confirma tus preferencias.
   * Dirigirse al Index.
   * Ahora vamos a buscar preferencias haciendo click sobre "Buscar Preferencias" en la navbar.
   * Ingresando un Lenguaje (recomendamos buscar Html por mayor cantidad de datos agregados al momento) y presionando buscar apareceran los resultados.
   * Dirigirse al Index.
   * Ahora vamos a ver el Blog Index, Hacemos click sobre Blog/Blog Home en la navbar.
   * Vas a ver una web donde se muestran los posteos realizados por los usuarios del blog.
   * Tambien podemos crear un post nosotros y para ello necesitamos ingresar a Blog/Blog Post en la navbar.
   * Aqui veremos un formulario donde llenaremos los datos del Posteo a realizar (en imagen utilizar una url)
   * Para ver el post creado debemos volver a Blog Home y aparecera en el inicio, haciendo un click podemos acceder para ver el contenido agregado de manera ordenada.
   * En la navbar podemos acceder a la sección Juegos
   * En sección juegos debemos primeramente añadir genero, desarrollador y plataforma, luegos podremos generar juegos para visualizarlos en el inicio
   * En el inicio ademas de visualizar los post de juegos creados, podemos buscar juegos por su nombre y accesder a las distintas secciones del Blog Juegos
  
  
<br></br>
<h2 aling="center" >Futuros cambios</h2>

* Debemos revisar la totalidad de los enlaces para que funcionen absolutamente todos con {% url 'urls' %}.
* Identificar los Try: Except: mas importantes para implementar (Caracteres no validos en formularios , Formularios incompletos , Busqueda de elementos de objetos no existentes , Urls inexistentes).
* Establecer tamaños de imagenes estaticos para distintas partes de la web.
* Un modelo de comentarios para aplicar esta funcionalidad.
* Colocar imagenes faltantes y reemplazo de Lorem.
* Establecer Login y Logout.
* Enlazar Registro de Usuarios con Preferencias atravez de Foreign Key.
* Permitir solamente valores unicos en Registro de Usuarios.
* Posibilidad de editar / borrar posteos realizados.
* Establecer permisos de usuarios.
* En los post queda agregar al autor de dicho blog
* Tememos problemas con el menu desplegable en el extend de Buscar Preferencias.
