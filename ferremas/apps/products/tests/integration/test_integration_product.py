import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.products.models import Producto
from rest_framework import status

@pytest.mark.django_db
def test_create_product_api():
    """
    Esta prueba valida que se pueda crear un producto a la base de datos.
    """
    User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')
    response = client.post('/productos/', {'codigo': 1, 'marca': 'Prueba','nombre': 'Producto de prueba', 'precio': 100.0, 'stock': 50}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['codigo'] == 1

@pytest.mark.django_db
def test_get_product_list_api():
    """
    Esta prueba valida que se retorne un lista de objetos al consultar a la api.
    """
    Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    Producto.objects.create(codigo=2, marca= 'Prueba' , nombre='Producto 2', precio=20.0, stock=200)
    client = APIClient()
    response = client.get('/productos/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_product_detail_api():
    """
    Esta prueba valida que se retorne un detalle de un producto en particular.
    """
    producto = Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    client = APIClient()
    response = client.get(f'/productos/view/{producto.codigo}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['codigo'] == 1

@pytest.mark.django_db
def test_delete_product_api():
    """
    Esta prueba valida que se elimine de manera satisfactoria un producto de la base de datos.
    """
    User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')
    producto = Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    response = client.delete(f'/productos/view/{producto.codigo}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Producto.objects.filter(id=producto.id).count() == 0

@pytest.mark.django_db
def test_producto_inexistente():
    """
    Esta prueba verifica que se devuelva un error 404 cuando se intente acceder a un producto inexistente.
    """
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    codigo_inexistente = 999
    response = client.get(f'/productos/view/{codigo_inexistente}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_update_product_api():
    """
    Esta prueba verificar que se pueda acutalizar un producto exitosamente.
    """
    producto = Producto.objects.create(codigo=1234, nombre='Producto de prueba', precio=10.0, stock=100)
    client = APIClient()
    url = f'/productos/update/{producto.id}/'
    data = {
        "codigo": 4321,
        "marca": "1123asd",
        "nombre": "Producto Actualizado",
        "precio": 15.0,
        "stock": 50
    }
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['nombre'] == 'Producto Actualizado'
    assert response.data['precio'] == 15.0
    assert response.data['stock'] == 50