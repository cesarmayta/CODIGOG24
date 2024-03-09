from rest_framework import viewsets

from .models import (
    Category,Kind,
    Person,
    Priority,Status,
    Subkind,
    Ticket
)

from .serializers import (
    CategorySerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer