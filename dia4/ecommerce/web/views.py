from django.shortcuts import render,redirect

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
from .cart import Cart

def carrito(request):
    return render(request,'carrito.html')

def agregar_carrito(request,producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1
        
    obj_producto = Producto.objects.get(pk=producto_id)
    producto_imagenes = ProductoImagen.objects.filter(producto=obj_producto)
    print(producto_imagenes[0])
    carrito = Cart(request)
    carrito.add(obj_producto,cantidad,producto_imagenes[0].imagen.url)
    
    if request.method == 'GET':
        return redirect('/')
    
    return render(request,'carrito.html')

def eliminar_carrito(request,producto_id):
    obj_producto = Producto.objects.get(pk=producto_id)
    carrito = Cart(request)
    carrito.delete(obj_producto)
    
    if request.GET.get('hd') == '1':
        return redirect('/')
    
    return render(request,'carrito.html')

def limpiar_carrito(request):
    carrito = Cart(request)
    carrito.clear()
    
    return render(request,'carrito.html')

########### USUARIO Y CLIENTE #########
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def crear_usuario(request):
    if request.method == "POST":
        data_usuario = request.POST['nuevo_usuario']
        data_password = request.POST['nuevo_password']
        
        obj_usuario = User.objects.create_user(username=data_usuario,
                                               password=data_password)
        if obj_usuario is not None:
            login(request,obj_usuario)
            return redirect('/cuenta')
        
    return render(request,'login.html')

def login_usuario(request):
    context = {}
    if request.method == "POST":
        data_usuario = request.POST['login_usuario']
        data_password = request.POST['login_password']
        
        obj_usuario = authenticate(request,
                                   username=data_usuario,
                                   password=data_password)
        if obj_usuario is not None:
            login(request,obj_usuario)
            return redirect('/cuenta')
        else:
            context ={
                'mensajeError':'Datos Incorrectos'
            }
        
    return render(request,'login.html',context)

def logout_usuario(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def cuenta_usuario(request):
    return render(request,'cuenta.html')