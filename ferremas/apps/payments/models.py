from django.db import models
from django.conf import settings
from apps.orders.models import Pedido

class Payment(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.id} - Pedido {self.pedido.id}"
