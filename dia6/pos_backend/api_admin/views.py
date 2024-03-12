from rest_framework import viewsets
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from rest_framework.permissions import IsAuthenticated

from api.models import(
    Mesa,Categoria,Plato
)

from api.serializers import (
    MesaSerializer,
    CategoriaSerializer,
    PlatoSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class PlatoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer