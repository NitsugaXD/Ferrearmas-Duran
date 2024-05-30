from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import Producto
from apps.products.serializers import ProductoSerializer

class InventoryView(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
