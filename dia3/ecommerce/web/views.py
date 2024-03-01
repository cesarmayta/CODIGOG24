from django.shortcuts import render

from .models import (
    Categoria,Marca,Producto,
    ProductoImagen
)

############### CATALOGO DE PRODUCTOS #####################
def index(request):
    lista_categorias = Categoria.objects.all()
    lista_marcas = Marca.objects.all()
    
    categoria_id = request.GET.get('cat')
    marca_id = request.GET.get('mar')
    if categoria_id:
        categoria_seleccionada = Categoria.objects.get(pk=categoria_id)
        lista_productos = Producto.objects.filter(categoria=categoria_seleccionada)
    elif marca_id:
        marca_seleccionada = Marca.objects.get(pk=marca_id)
        lista_productos = Producto.objects.filter(marca=marca_seleccionada)
    else:
        lista_productos = Producto.objects.all()
    
    context = {
        'categorias':lista_categorias,
        'marcas':lista_marcas,
        'productos':lista_productos
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    obj_producto = Producto.objects.get(pk=producto_id)
    context = {
        'producto':obj_producto
    }
    return render(request,'producto.html',context)

########### CARRITO DE COMPRAS ############################
def carrito(request):
    return render(request,'carrito.html')
