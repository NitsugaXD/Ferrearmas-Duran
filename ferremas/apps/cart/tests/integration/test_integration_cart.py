import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from apps.products.models import Producto
from apps.cart.models import Carro, CarroProducto
from rest_framework import status


@pytest.mark.django_db
def test_agregar_productos_al_carro_success():
    """
    Esta prueba valida que se puedan agregar productos al carrito correctamente.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=20)
    url = reverse('agregar_productos_al_carro')
    data = {'codigo': 1, 'cantidad': 2}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['mensaje'] == f"Producto '{producto.nombre}' agregado correctamente al carro."

@pytest.mark.django_db
def test_eliminar_producto_del_carro():
    """
    Esta prueba valida que se pueda eliminar un producto del carrito correctamente.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    producto = Producto.objects.create(
        nombre='Producto de prueba',
        precio=10.0,
        codigo=1,
        stock=20
    )
    carro = Carro.objects.create(usuario=user)
    CarroProducto.objects.create(carro=carro, producto=producto, cantidad=2)
    url = reverse('eliminar_producto_del_carro', args=[producto.codigo])
    response = client.delete(url, format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not CarroProducto.objects.filter(carro=carro, producto=producto).exists()

@pytest.mark.django_db
def test_carro_detail_success():
    """
    Esta prueba valida que se pueda obtener el detalle del carrito correctamente.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    carro = Carro.objects.create(usuario=user)
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=20)
    CarroProducto.objects.create(carro=carro, producto=producto, cantidad=2)
    url = reverse('carro_detail')
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['productos']) == 1
    assert response.data['productos'][0]['nombre'] == 'Producto de prueba'
    assert response.data['total'] == 20.0

@pytest.mark.django_db
def test_carro_detail_carro_no_existe():
    """
    Esta prueba valida que se retorne un error si se intenta obtener el detalle de un carrito que no existe.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('carro_detail')
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == "El carro no existe."
