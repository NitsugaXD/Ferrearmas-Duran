from django.urls import path
from .views import PagarYFinalizarCarro

urlpatterns = [
    path('finalizar/', PagarYFinalizarCarro.as_view(), name='pagar-y-finalizar-carro'),
]
