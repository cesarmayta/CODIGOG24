from django.http import JsonResponse

def index(request):
    context = {
        'status':True,
        'message':'mi primer api rest con django'
    }
    
    return JsonResponse(context)
