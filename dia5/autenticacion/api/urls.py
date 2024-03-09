from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('usuario',views.UsuarioView.as_view()),
    path('usuario/token',views.TokenView.as_view()),
    path('usuario/jwt',views.JWTView.as_view())
]