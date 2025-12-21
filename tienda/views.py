from django.shortcuts import render
from django.core.paginator import Paginator
from tienda.models import Producto

# Creacion de la vista

def catalogo(request):
    productos = Producto.objects.all().order_by('id') # mantener orden
    paginator = Paginator(productos, 10)  # mostrar 10 productos por pagina
    page_number = request.GET.get('page') # numero de paginas por url 
    productos = paginator.get_page(page_number) # mantener objetos en las paginas
    agregar_catalogo = {'catalogo': productos} # diccionario para enviar a la plantilla
    return render(request, 'home/catalogo.html', agregar_catalogo)
