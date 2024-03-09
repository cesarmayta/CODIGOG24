from django.urls import path

from . import views

urlpatterns = [
    path('mesa', views.MesaView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('plato',views.PlatoView.as_view()),
    path('categoria/<int:categoria_id>/platos',views.CategoriaPlatoView.as_view()),
    path('plato/search',views.SearchPlatoView.as_view()),
    path('plato/img/upload',views.UploadPlatoImgView.as_view()),
    path('pedido',views.PedidoRegisterView.as_view())
]
