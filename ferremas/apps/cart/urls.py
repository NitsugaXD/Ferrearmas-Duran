from django.urls import path
from .views import AgregarProductosAlCarro, CarroDetail

urlpatterns = [
    path('productos/', AgregarProductosAlCarro.as_view(), name='agregar-productos-carro'),
    path('detalle/', CarroDetail.as_view(), name='carro-detalle'),
]
