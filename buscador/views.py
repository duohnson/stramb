from django.shortcuts import render
from tienda.models import Producto
from django.core.paginator import Paginator
from django.db.models import Q

# buscador de items.

def buscar(request):
    query = request.GET.get('q', '') # obtener el termino de busqueda desde la URL
    productos = Producto.objects.filter(
        Q(nombre__icontains=query) | Q(descripcion__icontains=query)
    ).order_by('id')  # buscar en nombre y descripcion, ignorando mayusc/minusc

    paginator = Paginator(productos, 10)  # mostrar 10 productos por pagina
    page_number = request.GET.get('page')  # numero de pagina desde la URL
    productos_page = paginator.get_page(page_number)  # obtener los productos para la pagina actual

    contexto = {
        'query': query,
        'catalogo': productos_page,
        
    }
    return render(request, 'home/search.html', contexto)