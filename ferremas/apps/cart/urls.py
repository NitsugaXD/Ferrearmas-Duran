from django.urls import path
from .views import AgregarProductosAlCarro, CarroDetail

urlpatterns = [
    path('agregar-productos/', AgregarProductosAlCarro.as_view(), name='agregar_productos_al_carro'),
    path('carro-detalle/', CarroDetail.as_view(), name='carro_detail'),
]
