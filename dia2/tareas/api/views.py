from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'message':'api rest con vistas basadas en clases'
        }
        return Response(context)