from django.contrib import admin

# Register your models here.
from .models import (
    Categoria,Marca,Producto,
    ProductoImagen
)

admin.site.register(Categoria)
admin.site.register(Marca)
#admin.site.register(Producto)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','marca','precio')
    
from django.utils.html import format_html

@admin.register(ProductoImagen)
class ProductoImagenAdmin(admin.ModelAdmin):
    
    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))
    
    imagen_html.short_description = 'Image'
    
    list_display = ('producto','imagen_html')