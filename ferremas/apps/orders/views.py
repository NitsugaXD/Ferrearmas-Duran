from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Pedido, PedidoProducto
from apps.cart.models import Carro
from apps.products.models import Producto

class PagarYFinalizarCarro(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        usuario = request.user
        try:
            carro = Carro.objects.get(usuario=usuario)
        except Carro.DoesNotExist:
            return Response({"error": "Carro no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        total = sum(item.producto.precio * item.cantidad for item in carro.carroproducto_set.all())
        pedido = Pedido.objects.create(usuario=usuario, total=total, pagado=True)
        productos_nombres = []
        for item in carro.carroproducto_set.all():
            PedidoProducto.objects.create(pedido=pedido, producto=item.producto, cantidad=item.cantidad)
            productos_nombres.append({
                'nombre': item.producto.nombre,
                'cantidad': item.cantidad,
                'precio': item.producto.precio,
                'total': item.producto.precio * item.cantidad
            })
        carro.carroproducto_set.all().delete()
        return Response({
            "mensaje": "Carro pagado y pedido finalizado correctamente.",
            "total": total,
            "carro": productos_nombres
        }, status=status.HTTP_200_OK)
