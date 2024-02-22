"""
URL configuration for misitioweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse('<h1>Hola mundo con Django</h1>')

def api(request):
    context = {
        'status':True,
        'message':'api rest con django'
    }

    return JsonResponse(context)

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse(f'<h1> Hola {nombre}</h1>')

def sumar(request,n1,n2):
    resultado = n1 + n2
    return HttpResponse(f'la suma de {n1} + {n2} es {resultado}')


def calculadora(request,ope,n1,n2):
    """
    implementar una ruta que pueda sumar,restar y multiplicar 2 números dependiendo de la operación
    """
    pass

urlpatterns = [
    path('',index),
    path('api',api),
    path('sumar/<int:n1>/<int:n2>',sumar),
    path('saludo',saludo),
    path('admin/', admin.site.urls),
]
