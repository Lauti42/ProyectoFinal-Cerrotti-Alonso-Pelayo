<em>Entrega1-   Cerrotti  Pelayo   Alonso </em>

<h1 aling="center" >Primera entrega del Proyecto Final.</em>

### Indice:

:page_facing_up:Templates:
* Inicio.
* Registro
* Registrado / Registrar Preferencias
* Preferencias Agregadas
* Buscar Preferencias
* About
* Blog Index
* Blog Post
* Blog View

:wrench:Modelos:

* Modelo de Registro
* Modelo de Preferencias
* Modelo de Blog

:spiral_notepad:Formularios: 
* Formulario de Preferencias

:abc:Orden de Prueba:
* Registro / Preferencias / Busqueda / Blog.

:hammer:Funcionalidades del proyecto
* :hammer:Registrar usuarios. Tenemos la funcionalidad de guardar datos que ingresan nuestros usuarios en la Base de datos.
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
* :hammer:Filtrar preferencias. Tenemos la funcionalidad de revisar las preferencias de nuestros usuarios.
* :hammer:Realizar Posteos. Tenemos la funcionalidad de realizar posteos, reflejarlos en la Base de datos y mostrarlos a eleccion dentro de todo el sitio.

<br></br>

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
    
6) Template / About:
    
    
    
    * Es un template individual , contiene una descripcion individual de cada uno de los integrantes
    * Al final del template se puede econtrar una seccion donde Estan los integrantes.
    <br></br>
    
7) Template / Blog Index: 
    
    [![Blog-Index-Nuevo.png](https://i.postimg.cc/XYXHkNsv/Blog-Index-Nuevo.png)](https://postimg.cc/CRTsF0Ty)
    
    * Blog Index es un template Individual , contiene una navbar propia.
    * El proposito de Blog Index es resaltar un Blog de nuestra eleccion  (Mas informacion en Models) y mostrar todos los blogs creados por los usuarios.
    <br></br>
 
8) Template / Blog Post: 
    
    [![Blog-Post.png](https://i.postimg.cc/fLMY5BMv/Blog-Post.png)](https://postimg.cc/yJrJ8hgJ)
    
    * Blog Post es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede agregar un autor , contenido , imagen , asunto.
    <br></br>
    
9) Template / Blog View:
    
    [![Blog-Publicado.png](https://i.postimg.cc/W3pJ0z7W/Blog-Publicado.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Blog 
    * Renderiza Autor,Contenido,Imagen y asunto.
    <br></br>
    

   
 
