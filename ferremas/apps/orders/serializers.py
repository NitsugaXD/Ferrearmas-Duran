from rest_framework import serializers
from .models import Pedido
from apps.products.serializers import ProductoSerializer

class PedidoSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'fecha_creacion', 'productos', 'total', 'pagado']
