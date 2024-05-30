from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Carro, CarroProducto
from .serializers import CarroSerializer, CarroProductoSerializer
from apps.products.models import Producto

class AgregarProductosAlCarro(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        usuario = request.user
        carro, created = Carro.objects.get_or_create(usuario=usuario)
        serializer = CarroProductoSerializer(data=request.data)
        if serializer.is_valid():
            codigo = serializer.validated_data['codigo']
            cantidad = serializer.validated_data['cantidad']
            try:
                producto = Producto.objects.get(codigo=codigo)
            except Producto.DoesNotExist:
                return Response({"error": f"Producto con código {codigo} no existe."}, status=status.HTTP_404_NOT_FOUND)

            carro_producto, created = CarroProducto.objects.get_or_create(carro=carro, producto=producto, defaults={'cantidad': cantidad})
            if created:
                carro_producto.cantidad = cantidad
            else:
                carro_producto.cantidad += cantidad
            carro_producto.save()

            return Response({"mensaje": f"Producto '{producto.nombre}' agregado correctamente al carro."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarroDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        usuario = request.user
        try:
            carro = Carro.objects.get(usuario=usuario)
        except Carro.DoesNotExist:
            return Response({"error": "El carro no existe."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarroSerializer(carro)
        total = sum(item['precio'] * item['cantidad'] for item in serializer.data['productos'])
        response_data = {
            'productos': serializer.data['productos'],
            'total': total
        }
        return Response(response_data, status=status.HTTP_200_OK)
