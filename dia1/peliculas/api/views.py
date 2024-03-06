from django.http import JsonResponse
from .models import Pelicula

def index(request):
    context = {
        'status':True,
        'message':'mi primer api rest con django'
    }
    
    return JsonResponse(context)

def pelicula(request):
    lista_peliculas = Pelicula.objects.all()
    
    context = {
        'status':True,
        'content':list(lista_peliculas.values())
    }
    
    return JsonResponse(context)