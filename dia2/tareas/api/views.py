from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tarea
from .serializers import TareaSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'message':'api rest con vistas basadas en clases'
        }
        return Response(context)
    
class TareaView(APIView):
    
    def post(self,request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        context = {
            'status':True,
            'content':serializer.data
        }
        return Response(context)