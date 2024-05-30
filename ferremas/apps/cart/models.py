from django.db import models
from django.conf import settings
from apps.products.models import Producto

class Carro(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarroProducto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class CarroProducto(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('carro', 'producto')
