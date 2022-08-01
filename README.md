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
   
   [![Index-Nuevo.png](https://i.postimg.cc/vHVQBMdp/Index-Nuevo.png)](https://postimg.cc/GHb07WtQ)
   
   * En el index podemos encontrar un encabezado donde nos da la Bienvenida
   * Podemos encontrar una barra de navegacion que nos guiara a cada una de nuestras funcionalidades.
   * En la parte inferior de el Index se muestran los blogs que nosotros elegimos para mostrar (mas informacion en Models)
   * Dentro del encabezado existen 2 botones que nos redirigen al formulario de Registro y al About.
   
    Proximo a implementar:
   * Construir la funcionalidad para que el usuario coloque su email para que nosotros podamos contactarlo.
   <br></br>
   
2) Templates / Registro:
    
    [![Registro-Primer-formulario.png](https://i.postimg.cc/s2wBcyxT/Registro-Primer-formulario.png)](https://postimg.cc/p95XWwDj)
    
    * El template de Registro , es una extencion del Index , se agrega unicamente Un formulario y una generalizacion de las actividades que se pueden realizar.
    <br></br>
    
3) Templates / Registrado / Registrar Preferencias:
    
    [![Blog-registro-OK-Agregar-Preferencias.png](https://i.postimg.cc/YSY7rxKY/Blog-registro-OK-Agregar-Preferencias.png)](https://postimg.cc/f3zp5mbR)
    
    * El template de Registrar preferencias es la Extencion del Index y es una renderizacion de la vista registrar.
    * Se agrega una descripcion donde explicamos para que utilizamos las preferencias y por debajo un formulario para agregarlas.
    <br></br>
 
4) Templates / Preferencias Agregadas:
    
    [![Preferencias-Agregadas.png](https://i.postimg.cc/02nd3gzJ/Preferencias-Agregadas.png)](https://postimg.cc/SJXM2v7y)
    
    * El template es una extencion de Index , se agrega solamente un mensaje de Confirmacion.
    <br></br>
    
5) Templates / Buscar Preferencias:
    
    [![Busqueda-Preferencias.png](https://i.postimg.cc/WbYqgsDS/Busqueda-Preferencias.png)](https://postimg.cc/kB85d3vt)
    
    * El template es una extencion del Index , unicamente se conserva la navbar y se agrega un formulario para buscar las preferencias atravez de un Lenguaje.
    <br></br>
    
6) Templates / Resultados Preferencias:
      
      [![Resultado-Busqueda-Preferencias.png](https://i.postimg.cc/K8qYCf7N/Resultado-Busqueda-Preferencias.png)](https://postimg.cc/JsXmkb2D)
      
      * El template es una extencion del Index , unicamente se conserva la navbar y se agregan listas que muestran los resultados de la busqueda.
    
7) Templates / About:
    
    
    
    * Es un template individual , contiene una descripcion individual de cada uno de los integrantes
    * Al final del template se puede econtrar una seccion donde Estan los integrantes.
    <br></br>
    
8) Templates / Blog Index: 
    
    [![Blog-Index-Nuevo.png](https://i.postimg.cc/XYXHkNsv/Blog-Index-Nuevo.png)](https://postimg.cc/CRTsF0Ty)
    
    * Blog Index es un template Individual , contiene una navbar propia.
    * El proposito de Blog Index es resaltar un Blog de nuestra eleccion  (Mas informacion en Models) y mostrar todos los blogs creados por los usuarios.
    <br></br>
 
9) Templates / Blog Post: 
    
    [![Blog-Post.png](https://i.postimg.cc/fLMY5BMv/Blog-Post.png)](https://postimg.cc/yJrJ8hgJ)
    
    * Blog Post es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede agregar un autor , contenido , imagen , asunto.
    <br></br>
    
10) Templates / Blog View:
    
    [![Blog-Publicado.png](https://i.postimg.cc/W3pJ0z7W/Blog-Publicado.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Blog 
    * Renderiza Autor,Contenido,Imagen y asunto.
    <br></br>
   
11) Templates / Blog Juegos:
    
   [![imagen-2022-08-01-014426739.png](https://i.postimg.cc/Qdm58QbH/imagen-2022-08-01-014426739.png)](https://postimg.cc/mPchVFKs)
    
   * Entrada a la sección Juegos
   * Aqui se encuentran los ultimos juegos cargados
   * Se encuentra la entrada a visualizaciones de generos, desarrolladores, plataformas
   * Se encuentra boton de busqueda de juegos
   <br></br>

12) Templates / Blog Juegos / Todos los juegos:
    
   [![imagen-2022-08-01-015047030.png](https://i.postimg.cc/bwhWchCq/imagen-2022-08-01-015047030.png)](https://postimg.cc/ykLvcwCG)
    
   * Vista de todos los juegos cargados
   <br></br>
   
13) Templates / Blog Juegos / Detalle de juegos:
    
   [![imagen-2022-08-01-015801911.png](https://i.postimg.cc/wvGZSRPr/imagen-2022-08-01-015801911.png)](https://postimg.cc/zbTxhvqw)
    
   * Detalle de los juegos cargados
   <br></br>

14) Templates / Blog Juegos / (generos, desarrolladores, plataformas):
    
   [![imagen-2022-08-01-014741515.png](https://i.postimg.cc/Wb3cYjHC/imagen-2022-08-01-014741515.png)](https://postimg.cc/grf7n9dH)
   [![imagen-2022-08-01-014758916.png](https://i.postimg.cc/MG1CfGnM/imagen-2022-08-01-014758916.png)](https://postimg.cc/wtTfSgcg)
   [![imagen-2022-08-01-014814592.png](https://i.postimg.cc/6qbgx2mS/imagen-2022-08-01-014814592.png)](https://postimg.cc/PvZ2mxhz)
    
   * Vista de cada uno de los modelos
   * Visual en construcción
   * Se encuentra boton de busqueda de cada sección (en un futuro de devolverla los juegos corrrepondientes a cada sección)
   * Cada modelo se puede editar, borrar y crear nuevos
   <br></br>
   
15) Templates / Blog Juegos / Resultado de busqueda:
    
   [![imagen-2022-08-01-015420557.png](https://i.postimg.cc/BZC1c5rN/imagen-2022-08-01-015420557.png)](https://postimg.cc/Z0CRJNKy)
    
   * Busqueda dependiendo del origen de la busqueda
   * Visual en construcción
   <br></br>


<br></br>
<h2 aling="center" >Modelos</h2>

 
1) Modelos / Registro_usuarios.
   
   ```Python 
   class Registro_usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre + " " + self.email
   ```
   * Nombre - Email - Contraseña - Create (Determina automaticamente la fecha de creacion del registro.)
     <br></br>
     
 2) Modelos / Preferencias_Usuario:
      
    ```Python
    class Preferencias_Usuario(models.Model):
    lenguaje = models.CharField(max_length=40)
    backOfront = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)

    def __str__(self):
        return self.lenguaje + " " + self.backOfront + " " + self.pais + " " + self.trabajo

    class Meta():
        verbose_name = "Preferencias"
    ```
    * Lenguaje - Backend o Frontend - Pail - Trabajo. 
      <br></br>
 
 3) Modelos / Blog Entry:
      
    ```Python  
    class Entry(models.Model):

    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('si', 'Si'),
        ('no', 'No'),
    )



    nombre = models.CharField(max_length=100)
    contenido = models.TextField(max_length=1000)
    imagen = models.URLField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')


    def __str__(self):
        return self.nombre + " - " + self.autor + " - " + str(self.fecha)
    ```
    * Nombre - Contenido - Imagen - Autor - Fecha (Se agrega de manera auto) - Publicado - Muestra Inferior (Determinamos si puede mostrarse o no debajo del index)
      Muestra superior (Determianmos si va a estar en el Header de Blog Index.)
 
 4) Modelos / Blog Juegos:
    
   ```Python  
    class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.pais}'
  ```
   ```Python 
   class Genero(models.Model):
       nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'
   ```
   ```Python 
    class Plataformas(models.Model):
      nombre = models.CharField(max_length=50)
      link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.link}'
   ```
   ```Python
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
        return f'{self.nombre} ({self.anodecreacion})'
   ```

    
<br></br>
<h2 aling="center" >Formularios</h2>


1) Formulario de Preferencias:
   
   ```Python
   class PreferenciasFormulario(forms.Form):

    lenguaje = forms.CharField()
    backofront = forms.CharField()
    pais = forms.CharField()
    trabajo = forms.CharField()
   ```
   
2) Formulario de Juegps:
   
   ```Python
   class DesarrolladorCreate(CreateView):
    model = Desarrollador
    template_name = "crea-desarrollador.html"
    fields = ["nombre", "pais"]
    success_url = "/juegos/desarrolladores/"
   ```
   
   ```Python
   class GeneroCreate(CreateView):
    model = Genero
    template_name = "crea-genero.html"
    fields = ["nombre"]
    success_url = "/juegos/generos/"
   ```
   
   ```Python
   class PlataformasCreate(CreateView):
    model = Plataformas
    template_name = "crea-plataforma.html"
    fields = ["nombre", "link"]
    success_url = "/juegos/plataformas/"
   ```
   
   ```Python
   class JuegosCreate(CreateView):
    model = Juegos
    template_name = "crea-juego.html"
    fields = ["nombre", "anodecreacion", "desarrollador", "genero", "plataforma", "urlimagen", "descripcion"]
    success_url = "/juegos/"
   ```
 + Formularios creados con Clases basadas en vistas

<br></br>
<h2 aling="center" >Funcionalidades del Proyecto</h2>

* :hammer:Registrar usuarios. Tenemos la funcionalidad de guardar datos que ingresan nuestros usuarios en la Base de datos.
   ```Python
   def registrarse(request):
    return render(request, 'registrarse.html')

   def registro(request):
    if request.method == 'POST':
        print("POST")

        #Obteniendo datos del registro (Form)
        nombre = request.POST['Usuario']
        email = request.POST['Email']
        password = request.POST['Contraseña']
        password2 = request.POST['Contraseña2']
    
        #Guardando los datos en la DB
        User_registred = Registro_usuarios(nombre=nombre, email=email, password=password)
        User_registred.save()
            
        documentoDeTexto = f"Integrante creado con exito: {nombre} {email} {password} {password2}"
        return render(request, "indexregistrado.html", {'documentoDeTexto': documentoDeTexto})
   ```
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
   ```Python
   def preferencias(request):
    if request.method == "POST":
        print("POST")
        #Obteniendo datos del registro (Form)
        preferenciasUsuarioForm = PreferenciasFormulario(request.POST)    
        
        if preferenciasUsuarioForm.is_valid():

            data = preferenciasUsuarioForm.cleaned_data

            #Guardando los datos en la DB
            Pref = Preferencias_Usuario(lenguaje=data["lenguaje"], backOfront=["backofront"], pais=["pais"], trabajo=["trabajo"])
            Pref.save()

        return render(request, "preferenciasenviadas.html")
   ```
* :hammer:Filtrar preferencias. Tenemos la funcionalidad de revisar las preferencias de nuestros usuarios.
   ```Python
   def buscarPreferencias(request):
    return render(request, 'buscarpreferencias.html')


   def resultadoPreferencias(request):
    if request.GET["lenguaje"]:

        lenguaje = request.GET["lenguaje"]
        preferencias = Preferencias_Usuario.objects.filter(lenguaje__icontains=lenguaje)

        return render(request, 'resultadopreferencias.html', {'preferencias': preferencias, 'lenguaje': lenguaje})
   ```
* :hammer:Realizar Posteos. Tenemos la funcionalidad de realizar posteos, reflejarlos en la Base de datos y mostrarlos a eleccion dentro de todo el sitio.
   ```Python
   class PostDetalle(DetailView):
    model = Entry
    context_object_name = 'post'
    template_name = 'GeneralPost.html'


   def NewPostSave(request):
    if request.method == 'POST':
        print("POST")
     #Obteniendo datos del registro (Form)
        nombre = request.POST['nombre']
        contenido = request.POST['contenido']
        imagen = request.POST['imagen']
        autor = request.POST['autor']
        
        #Guardando los datos en la DB
        Entrys = Entry(nombre=nombre, contenido=contenido, imagen=imagen, autor=autor)
        Entrys.save()
        
    return render(request, 'indexBase.html')


   def NewPost(request):
    return render(request, 'makeanewpost.html')


   def blog_general_index(self):

    post= Entry.objects.all()
    # post_sup= Entry.objects.filter(muestra_superior= 'si')
   

    return render(self, 'Blog_Generalindex.html', {'post': post})

   def verpost(request):
    print(request)
    return render(request, 'indexBase.html')
   ```
* :hammer:Listas con entrada a Detalles de los modelos. Tenemos la funcionalidad de ver la lista de los modelos creados y guardados en base de datos. Se pueden ver los detalles de cada modelo.

   ```Python
   def all_games(request):

    post= Juegos.objects.all()
    # post_sup= Entry.objects.filter(muestra_superior= 'si')
   

    return render(request, 'Blog_GeneralindexG.html', {'post': post})
    
   class JuegosList(ListView):
    
    model = Juegos
    template_name = "iniciojuegos.html"
    context_object_name= 'juegos'

   class JuegosDetail(DetailView):
    model = Juegos
    template_name = "GeneralPostG.html"
    context_object_name= 'juegos'
   ```
   ```Python
   class PlataformasList(ListView):
    
    model = Plataformas
    template_name = "lista-plataformas.html"
    context_object_name= 'plataformas'

   class PlataformasDetail(DetailView):
    model = Plataformas
    template_name = "detalle-plataforma.html"
    context_object_name= 'plataformas'
   ```
   ```Python
   class GeneroList(ListView):
    
    model = Genero
    template_name = "lista-generos.html"
    context_object_name= 'generos'

   class GeneroDetail(DetailView):
    model = Genero
    template_name = "detalle-genero.html"
    context_object_name= 'generos'
   ```
   ```Python
   class DesarrolladorList(ListView):
    
    model = Desarrollador
    template_name = "lista-desarrolladores.html"
    context_object_name= 'desarrollador'

   class DesarrolladorDetail(DetailView):
    model = Desarrollador
    template_name = "detalle-desarrollador.html"
    context_object_name= 'desarrollador'
   ```
   
* :hammer:Posibilidad de borrar y editar los modelos. Tenemos la funcionalidad de editar y eliminar los modelos guardados en base de datos.

   ```Python
   class JuegosUpdate(UpdateView):
    model = Juegos
    template_name = "edita-juego.html"
    fields = ('__all__')
    success_url = "/juegos/"

   class Juegosdelete(DeleteView):
    model = Juegos
    template_name = "eliminar-juego.html"
    success_url = "/juegos/"

   ```
   ```Python
   class PlataformasUpdate(UpdateView):
    model = Plataformas
    template_name = "edita-plataforma.html"
    fields = ('__all__')
    success_url = "/juegos/plataformas/"
    
   class Plataformasdelete(DeleteView):
    model = Plataformas
    template_name = "eliminar-plataforma.html"
    success_url = "/juegos/plataformas/"
   ```
   ```Python
   class GeneroUpdate(UpdateView):
    model = Genero
    template_name = "edita-genero.html"
    fields = ('__all__')
    success_url = "/juegos/generos/"
    
   class Generodelete(DeleteView):
    model = Genero
    template_name = "eliminar-genero.html"
    success_url = "/juegos/generos/"
   ```
   ```Python
   class DesarrolladorUpdate(UpdateView):
    model = Desarrollador
    template_name = "edita-desarrollador.html"
    fields = ('__all__')
    success_url = "/juegos/desarrolladores/"

   class Desarrolladordelete(DeleteView):
    model = Desarrollador
    template_name = "eliminar-desarrollador.html"
    success_url = "/juegos/desarrolladores/"
   ```
   
* :hammer:Buscar por nombre de modelo. Tenemos la posibilidad de buscar por el nombre de cada modelos registrado en la base de datos.
   
   ```Python
   def buscar(request): 

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        juegos = Juegos.objects.filter(nombre__icontains=nombre)

        return render (request, "resultadoBusqueda.html", {"juegos": juegos, "nombre": nombre})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)
   ```
   
   ```Python
   def buscarplataforma(request): 

    if request.GET["plataforma"]:

        plataforma = request.GET["plataforma"]

        plataformas = Juegos.objects.filter(nombre__icontains=plataforma)

        return render (request, "resultadoBusqueda.html", {"plataformas": plataformas, "nombre": plataforma})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)
   ```
   
   ```Python
   def buscargenero(request): 

    if request.GET["genero"]:

        genero = request.GET["genero"]

        generos = Genero.objects.filter(nombre__icontains=genero)

        juegos = Juegos.objects.filter(genero__icontains=generos)

        return render (request, "resultadoBusqueda.html", {"generos": juegos, "nombre": genero})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)
   ```
   
   ```Python
   def buscardesarrollador(request): 

    if request.GET["desarrollador"]:

        desarrollador = request.GET["desarrollador"]

        desarrolladores = Desarrollador.objects.filter(nombre__icontains=desarrollador)

        return render (request, "resultadoBusqueda.html", {"desarrolladores": desarrolladores, "nombre": desarrollador})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)
   ```

   

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
