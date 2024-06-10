from django.db import models
from django.conf import settings
from apps.products.models import Producto

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'orders'
        
    def __str__(self):
        return f"Pedido {self.id}"

class PedidoProducto(models.Model):  # Renamed to avoid conflicts
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        app_label = 'orders'
        unique_together = ('pedido', 'producto')
        db_table = 'orders_pedido_producto'  # Specify a custom table name to avoid clashes
