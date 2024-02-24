from django.shortcuts import render

from .models import Tarea

# Create your views here.
def index(request):
    lista_tareas = Tarea.objects.all()
    print(lista_tareas)
    context = {
        'tareas':lista_tareas
    }
    return render(request,'index.html',context)
    