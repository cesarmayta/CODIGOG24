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

########### USUARIO Y LOGIN #########
from django.contrib.auth.models import User
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

############ CLIENTE ############
from .models import Cliente
from .forms import ClienteForm

@login_required(login_url='/login')
def cuenta_usuario(request):
    data = {}
    
    if request.user.first_name != '':
        data.update({'nombre':request.user.first_name})
        
    if request.user.last_name != '':
        data.update({'apellidos':request.user.last_name})
    
    data.update({'email':request.user.username})
    
    ### cargamos datos cliente
    try:
        obj_cliente = Cliente.objects.get(usuario=request.user)
        data_cliente = {
            'direccion':obj_cliente.direccion,
            'telefono':obj_cliente.telefono,
            'dni':obj_cliente.dni,
            'fecha_nacimiento':obj_cliente.fecha_nacimiento,
            'sexo':obj_cliente.sexo
        }
    except:
        data_cliente = {
            'direccion':'',
            'telefono':'',
            'dni':'',
            'fecha_nacimiento':'',
            'sexo':'M'
        }
    
    data.update(data_cliente)
    
    form_cliente = ClienteForm(data)
    context = {
        'frm_cliente':form_cliente
    }
    return render(request,'cuenta.html',context)

def actualizar_cliente(request):
    if request.method == "POST":
        frm_cliente = ClienteForm(request.POST)
        if frm_cliente.is_valid():
            data = frm_cliente.cleaned_data
            
            #actualizamos usuario
            obj_usuario = User.objects.get(pk=request.user.id)
            obj_usuario.first_name = data['nombre']
            obj_usuario.last_name = data['apellidos']
            obj_usuario.email = data['email']
            obj_usuario.save()
            
            try:
                obj_cliente = Cliente.objects.get(usuario=obj_usuario)
            except:
                obj_cliente = Cliente()
                obj_cliente.usuario = obj_usuario
                
            obj_cliente.dni = data['dni']
            obj_cliente.direccion = data['direccion']
            obj_cliente.telefono = data['telefono']
            obj_cliente.fecha_nacimiento = data['fecha_nacimiento']
            obj_cliente.sexo = data['sexo']
            obj_cliente.save()
            mensaje = 'Datos Guardados'
            
    return redirect('/cuenta')

#### PEDIDO ######
from .models import Pedido,PedidoDetalle

@login_required(login_url='/login')
def registrar_pedido(request):
    data_cliente = {}
    
    data_usuario = {
        'nombre':request.user.first_name,
        'apellidos':request.user.last_name,
        'email':request.user.email
    }
    
    data_cliente.update(data_usuario)
    
    
    form_cliente = ClienteForm(data_cliente)
    context = {
        'frm_cliente':form_cliente
    }
    return render(request,'pedido.html',context)