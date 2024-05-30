from rest_framework import serializers
from .models import Carro, CarroProducto
from apps.products.serializers import ProductoSerializer

class CarroProductoSerializer(serializers.ModelSerializer):
    codigo = serializers.ReadOnlyField(source='producto.codigo')
    nombre = serializers.ReadOnlyField(source='producto.nombre')
    precio = serializers.ReadOnlyField(source='producto.precio')

    class Meta:
        model = CarroProducto
        fields = ['codigo', 'nombre', 'precio', 'cantidad']

class CarroSerializer(serializers.ModelSerializer):
    productos = CarroProductoSerializer(source='carroproducto_set', many=True)

    class Meta:
        model = Carro
        fields = ['id', 'productos', 'fecha_creacion']
