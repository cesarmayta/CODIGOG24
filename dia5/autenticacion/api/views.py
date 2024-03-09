from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import (
    BasicAuthentication
)

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'message':'acceso publico'
        }
        return Response(context)