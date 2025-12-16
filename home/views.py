from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, 'home/index.html')
'''

    * Funcion de vista, su trabajo es recibir una solicitud web, procesarla, y devolver una respuesta adecuada.
Donde 'index y 'contacto son el nombre de las funciones, y 'request es parametro obligatorio donde toda funcion
de VISTA debe aceptar.
    * 'request' Dentro de funcion es basicamente, HttpRequest, objeto de clase que DJANGO utiliza cada que un usuario
pide una pagina web, http en este caso.
    * 'return' Donde devuelve la respuesta http al solicitante
    * 'render' Auxiliar para devolver una respuesta que involucra una plantilla
Se deben usar estas funciones para cargar las vistas de una nueva app en proyecto.

'''

def contacto(request):
    return render(request, 'home/contacto.html')
