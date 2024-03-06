from django.http import JsonResponse
from .models import Pelicula

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    context = {
        'status':True,
        'message':'mi primer api rest con django'
    }
    
    return Response(context)

def pelicula(request):
    lista_peliculas = Pelicula.objects.all()
    
    context = {
        'status':True,
        'content':list(lista_peliculas.values())
    }
    
    return JsonResponse(context)

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registrar_pelicula(request):
    json_data = json.loads(request.body)
    
    titulo = json_data['titulo']
    imagen = json_data['imagen']
    
    obj_pelicula = Pelicula.objects.create(
        titulo=titulo,
        imagen=imagen
    )
    
    dic_curso = {
        'id':obj_pelicula.id,
        'titulo':obj_pelicula.titulo,
        'imagen':obj_pelicula.imagen
    }
    
    context = {
        'status':True,
        'message':'pelicula registrada',
        'content':dic_curso
    }
    
    return JsonResponse(context)