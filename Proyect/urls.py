"""
URL configuration for Proyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # imagenes
from django.conf.urls.static import static # imagenes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Agregamos la ruta de la carpeta home al principal.
    #path('usuarios/', include('usuarios.urls')),
    #path('accounts/', include('django.contrib.auth.urls')), # Rutas de autenticacion
    #path('accounts/', include('usuarios.urls')), # Rutas personalizadas de usuarios
    path('catalogo/', include('tienda.urls')), # Agregamos la ruta de la carpeta tienda al principal.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)