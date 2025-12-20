from django.shortcuts import render
from tienda.models import Producto

# Creacion de la vista

def catalogo(request):
    productos = Producto.objects.all()
    agregar_catalogo = {'catalogo': productos}
    return render(request, 'home/catalogo.html', agregar_catalogo)
