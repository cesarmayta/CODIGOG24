from django.contrib import admin

# Register your models here.
from .models import (
    Categoria,Mesa,
    Plato
)

admin.site.register(Categoria)
admin.site.register(Mesa)
admin.site.register(Plato)


