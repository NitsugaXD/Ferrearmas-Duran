from django.urls import path
from .views import AgregarProductosAlCarro, CarroDetail, eliminar_producto_del_carro

urlpatterns = [
    path('agregar-productos/', AgregarProductosAlCarro.as_view(), name='agregar_productos_al_carro'),
    path('carro-detalle/', CarroDetail.as_view(), name='carro_detail'),
    path('eliminar_producto_del_carro/<int:producto_id>/', eliminar_producto_del_carro, name='eliminar_producto_del_carro'),
]
