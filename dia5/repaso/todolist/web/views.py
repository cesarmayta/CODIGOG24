from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import Tarea

# Create your views here.
def index(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Tarea.objects.create(descripcion=descripcion)
    
    lista_tareas = Tarea.objects.all()
    print(lista_tareas)
    context = {
        'tareas':lista_tareas
    }
    return render(request,'index.html',context)

def editar_tarea(request,id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(pk=id)
        descripcion = request.POST.get('descripcion')
        tarea.descripcion = descripcion
        tarea.save()
        return redirect('/')
        
    tarea = Tarea.objects.get(pk=id)
    lista_tareas = Tarea.objects.all()
    context = {
        'tareas':lista_tareas,
        'tarea_editar':tarea
    }
    return render(request,'index.html',context)


def eliminar_tarea(request,id):
    tarea = Tarea.objects.get(pk=id)
    tarea.delete()
    return redirect('/')
    
def completar_tarea(request,id):
    tarea = Tarea.objects.get(pk=id)
    tarea.estado = 'completado'
    tarea.save()
    return redirect('/')

def toogle_estado_tarea(request,id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(pk=id)
        if tarea.estado == 'pendiente':
            tarea.estado = 'completado'
        else:
            tarea.estado = 'pendiente'
        tarea.save()
        context = {
            'estado':tarea.estado
        }
        return JsonResponse(context)
    
    context = {
        'error':'petición invalida'
    }
    return JsonResponse(context)