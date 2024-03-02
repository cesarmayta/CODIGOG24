from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models

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
    list_display = ('sku','nombre','categoria','marca','precio')
    list_filter = ('categoria','marca')
    
    formfield_overrides = {
        models.TextField :{'widget':CKEditorWidget},
    }
    
from django.utils.html import format_html

@admin.register(ProductoImagen)
class ProductoImagenAdmin(admin.ModelAdmin):
    
    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))
    
    imagen_html.short_description = 'Imagen'
    
    list_display = ('orden','producto','imagen_html')
    search_fields = ['producto__nombre']