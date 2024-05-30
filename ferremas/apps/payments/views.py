from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from apps.orders.models import Pedido

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        usuario = request.user
        pedido_id = request.data.get('pedido_id')
        metodo_pago = request.data.get('metodo_pago')
        try:
            pedido = Pedido.objects.get(id=pedido_id, usuario=usuario)
        except Pedido.DoesNotExist:
            return Response({"error": "Pedido no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        payment = Payment.objects.create(pedido=pedido, metodo_pago=metodo_pago, usuario=usuario)
        return Response({"mensaje": "Pago realizado correctamente.", "payment": PaymentSerializer(payment).data}, status=status.HTTP_200_OK)
