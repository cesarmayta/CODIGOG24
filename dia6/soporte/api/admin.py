from django.contrib import admin

# Register your models here.
from .models import (
    Category,Kind,
    Person,
    Priority,Status,
    Subkind,
    Ticket
)

admin.site.register(Category)
admin.site.register(Kind)
admin.site.register(Subkind)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Person)
admin.site.register(Ticket)
