from django.urls import path, include
from .views import *
from usuario.views import Login,logoutUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('consultar/', Consultar_Producto.as_view(), name = 'consultar_producto'),
    path('consultaCart/',Consultar_Carrito.as_view(),name= 'consultar_carrito'),
    path('eliminarCarrito/<int:pk>/',EliminiarCarrito.as_view(),name= 'eliminarCarrito'),
    path('PagarCarrito/',PagarCarrito.as_view(),name= 'PagarCarrito'),
    path('cesta/<int:pk>', Carrazo.as_view(),name= 'cesta'),
    path('mujer/', productosMujer.as_view(),name= 'mujer'),
    path('hombre/', productosHombre.as_view(),name= 'hombre'),
    path('PagarCarrito/',PagarCarrito.as_view(),name= 'PagarCarrito'),
    
]
