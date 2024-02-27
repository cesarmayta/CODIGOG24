from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_categoria'
        
    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_marca'
        
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    marca = models.ForeignKey(Marca,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_producto'
        
    def __str__(self):
        return self.nombre
    
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_producto_imagen'
        
    def __str__(self):
        return str(self.imagen)
    