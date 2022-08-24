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

from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from Blog_General.models import Publicacion
from Main.views import aboutview, contactview, indexview
from RegistroUsuarios.views import login_request

from .views import Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_request, name= 'login'),
    path('index/', indexview, name='index'),
    path('registrado/', include('RegistroUsuarios.urls'),name='registrado'),
    path('registrarse/', include('RegistroUsuarios.urls'),name='registrarse'),
    path('about/', aboutview, name='about'),
    path('contact/', contactview, name='contact'),
    path('preferencias/', include('RegistroUsuarios.urls'),name='preferencias'),
    path('blog/', include('Blog_General.urls'),),
    path('logout/', LogoutView.as_view(template_name='indexBase.html'),{'posteos': Publicacion.objects.filter(muestra_inferior="si")}, name="logout"),
    
    
]

handler404 = Error404View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)