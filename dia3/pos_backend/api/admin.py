from django.contrib import admin

# Register your models here.
from .models import (
    Categoria,Mesa
)

admin.site.register(Categoria)
admin.site.register(Mesa)


