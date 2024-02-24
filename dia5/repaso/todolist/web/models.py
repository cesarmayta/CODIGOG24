from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now=True)
    estado = models.CharField(max_length=20)