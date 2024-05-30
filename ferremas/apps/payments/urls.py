from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('pagar/', PaymentView.as_view(), name='pago'),
]
