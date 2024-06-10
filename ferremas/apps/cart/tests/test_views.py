import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from apps.products.models import Producto
from apps.cart.models import Carro, CarroProducto

@pytest.mark.django_db
def test_agregar_productos_al_carro():
    client = APIClient()

    # Crear un usuario de prueba y autenticarlo
    user = User.objects.create_user(username='testuser', password='testpass')
    client.force_authenticate(user=user)

    # Crear un producto de prueba
    producto = Producto.objects.create(codigo='1234', nombre='Test Product', precio=10.0, stock=100)

    # Datos a enviar en la solicitud POST
    data = {
        'codigo': '1234',
        'cantidad': 2
    }

    # Realizar la solicitud POST para agregar el producto al carro
    response = client.post(reverse('agregar-producto'), data, format='json')

    # Verificar la respuesta
    assert response.status_code == status.HTTP_200_OK
    assert response.data['mensaje'] == f"Producto '{producto.nombre}' agregado correctamente al carro."

    # Verificar que el producto ha sido agregado al carro
    carro = Carro.objects.get(usuario=user)
    assert carro.productos.count() == 1
    carro_producto = CarroProducto.objects.get(carro=carro, producto=producto)
    assert carro_producto.cantidad == 2

@pytest.mark.django_db
def test_carro_detail():
    client = APIClient()

    # Crear un usuario de prueba y autenticarlo
    user = User.objects.create_user(username='testuser', password='testpass')
    client.force_authenticate(user=user)

    # Crear un producto y agregarlo al carro
    producto = Producto.objects.create(codigo='1234', nombre='Test Product', precio=10.0, stock=100)
    carro = Carro.objects.create(usuario=user)
    CarroProducto.objects.create(carro=carro, producto=producto, cantidad=2)

    # Realizar la solicitud GET para obtener los detalles del carro
    response = client.get(reverse('carro-detail'), format='json')

    # Verificar la respuesta
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['productos']) == 1
    assert response.data['productos'][0]['nombre'] == 'Test Product'
    assert response.data['productos'][0]['cantidad'] == 2
    assert response.data['total'] == 20.0  # 10.0 (precio) * 2 (cantidad)
