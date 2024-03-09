from rest_framework import viewsets

from .models import (
    Category,Kind,
    Person,
    Priority,Status,
    Subkind,
    Ticket
)

from .serializers import (
    CategorySerializer,
    KindSerializer,
    SubkindSerializer,
    PrioritySerializer,
    StatusSerializer,
    PersonSerializer,
    TicketSerializer
)

class KindViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    
class SubkindViewSet(viewsets.ModelViewSet):
    queryset = Subkind.objects.all()
    serializer_class = SubkindSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    