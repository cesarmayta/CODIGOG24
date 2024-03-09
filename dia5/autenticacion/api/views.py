from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import (
    BasicAuthentication,SessionAuthentication
)

from rest_framework.permissions import (
    IsAuthenticated
)

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'message':'acceso publico'
        }
        return Response(context)
    
class UsuarioView(APIView):
    authentacion_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'status':True,
            'usuario':str(request.user)
        }
        return Response(context)