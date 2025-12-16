from django.urls import path # Obligatorio en todas las apps o modulos.
from . import views # Importamos views de la carpeta home, ya que el . es igual a ./home/ y solicitamos a views

urlpatterns = [
    path('', views.index, name='index'), # Ruta principal, donde ubica index
    # Como se ve, esta vacia '' ya que indica ser ruta RAIZ.
    path('contacto/', views.contacto, name='contacto'), # Ruta de contacto, a llamada de contacto
]

'''

NoReverseMatch - En caso de este error, revise name='nombre de app' 
en ruta urls y que tenga coincidencia con views.

'''