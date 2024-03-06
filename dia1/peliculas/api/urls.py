from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('pelicula',views.pelicula),
    path('pelicula/add',views.registrar_pelicula)
]