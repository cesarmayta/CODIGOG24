"""
URL configuration for proyecto project.

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
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>mi pagina web</h1>')

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse(f'hola {nombre}')

def sumar(request,n1,n2):
    resultado = n1 + n2
    return HttpResponse(f'la suma de {n1} y {n2} es {resultado}')

def calculadora(request,ope,n1,n2):
    if(ope=="suma"):
        resultado = n1 + n2
        return HttpResponse(f'la suma de {n1} + {n2} es {resultado}')
    elif(ope == "resta"):
        resultado = n1 - n2
        return HttpResponse(f'la resta de {n1} - {n2} es {resultado}')
    elif(ope == "multiplicacion"):
        resultado = n1 * n2
        return HttpResponse(f'la suma de {n1} x {n2} es {resultado}')
    else:
        return HttpResponse('no se encontro la operación solicitada')

from peliculas.views import peliculas

urlpatterns = [
    path('',index),
    path('saludo',saludo),
    path('calculadora/<ope>/<int:n1>/<int:n2>',calculadora),
    path('sumar/<int:n1>/<int:n2>',sumar),
    path('peliculas',peliculas),
    path('admin/', admin.site.urls),
]
