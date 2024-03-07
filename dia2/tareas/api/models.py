from django.db import models

# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now=True)
    estado = models.ForeignKey(Estado,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.descripcion
    