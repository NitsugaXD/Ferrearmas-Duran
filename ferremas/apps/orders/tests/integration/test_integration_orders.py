import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from apps.products.models import Producto
from apps.cart.models import Carro, CarroProducto
from apps.orders.models import Pedido

# Prueba de integración para finalizar y pagar el carrito
@pytest.mark.django_db
def test_pagar_y_finalizar_carro():
    """
    Verifica que se pueda pagar y finalizar el carrito mediante la vista de API.
    """
    user = User.objects.create_user(username='testuser', password='testpass')
    producto1 = Producto.objects.create(nombre='Test Product 1', precio=100.00, codigo='1', stock=20)
    producto2 = Producto.objects.create(nombre='Test Product 2', precio=200.00, codigo='2', stock=20)
    carro = Carro.objects.create(usuario=user)
    CarroProducto.objects.create(carro=carro, producto=producto1, cantidad=1)
    CarroProducto.objects.create(carro=carro, producto=producto2, cantidad=2)

    client = APIClient()
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    client.force_authenticate(user=user)
    response = client.post('/orders/finalizar/', format='json')

    assert response.status_code == 200
    assert 'mensaje' in response.data
    assert 'total' in response.data
    assert 'carro' in response.data

    pedido = Pedido.objects.get(usuario=user)
    assert pedido.total == 500.00
    assert pedido.pagado == True
    assert pedido.productos.count() == 2
