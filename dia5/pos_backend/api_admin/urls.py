from rest_framework.routers import DefaultRouter
from django.urls import path,include

from . import views

router = DefaultRouter()

router.register(r'mesa',views.MesaViewSet,basename='mesas')

urlpatterns = [
    path('',include(router.urls)),
]