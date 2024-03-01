from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('',views.index,name='index'),
    path('producto/<int:producto_id>',views.producto,name='producto'),
    path('carrito',views.carrito,name='carrito'),
    path('carrito/add/<int:producto_id>',views.agregar_carrito,name='agregarcarrito'),
    path('carrito/del/<int:producto_id>',views.eliminar_carrito,name='eliminarcarrito')
]