from django.urls import path
from .views import AgregarProductosAlCarro, CarroDetail

urlpatterns = [
    path('agregar-producto/', AgregarProductosAlCarro.as_view(), name='agregar-producto'),
    path('carro/', CarroDetail.as_view(), name='carro-detail'),
]
