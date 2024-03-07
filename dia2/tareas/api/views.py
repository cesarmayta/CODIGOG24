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
    
    def get(self,request):
        data = Tarea.objects.all()
        serializer = TareaSerializer(data,many=True)
        context = {
            'status':True,
            'content':serializer.data
        }
        
        return Response(context)
    
    def post(self,request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        context = {
            'status':True,
            'content':serializer.data
        }
        return Response(context)
    

from django.http import Http404

class TareaDetailView(APIView):
    
    def get_object(self,pk):
        try:
            return Tarea.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self,request,pk):
        data = self.get_object(pk)
        serializer = TareaSerializer(data)
        return Response(serializer.data)
    
            