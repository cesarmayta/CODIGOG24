from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria,
    Plato
)

from .serializers import (
    CategoriaSerializer,
    MesaSerializer,
    PlatoSerializer,
    CategoriaPlatoSerializer
)

class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class MesaView(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    
class PlatoView(generics.ListCreateAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    
class CategoriaPlatoView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CategoriaPlatoSerializer
    
class SearchPlatoView(APIView):
    
    def post(self,request):
        search = request.data['search']
        data = Plato.objects.filter(plato_nom__contains=search)
        serializer = PlatoSerializer(data,many=True)
        return Response(serializer.data)
    
#### subir plato img
from rest_framework.parsers import MultiPartParser,JSONParser
import cloudinary.uploader

class UploadPlatoImgView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser
    )
    
    @staticmethod
    def post(request):
        file = request.data.get('plato_img')
        
        upload_data = cloudinary.uploader.upload(file)
        print(upload_data)
        context = {
            'url':upload_data['secure_url']
        }
        
        return Response(context)
    
    