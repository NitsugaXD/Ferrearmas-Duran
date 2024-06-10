from django.db import models

class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        app_label = 'products'
    def __str__(self):
        return self.nombre
