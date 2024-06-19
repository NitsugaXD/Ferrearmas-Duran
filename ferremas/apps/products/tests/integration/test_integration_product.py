import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.products.models import Producto

@pytest.mark.django_db
def test_create_product_api():
    # Crear un usuario administrador y autenticarlo
    user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')
    
    # Realizar la solicitud POST para crear un producto
    response = client.post('/productos/', {'codigo': 1, 'marca': 'Prueba','nombre': 'Producto de prueba', 'precio': 100.0, 'stock': 50}, format='json')
    
    # Verificar que la respuesta es 201 Created
    assert response.status_code == 201
    assert response.data['codigo'] == 1

@pytest.mark.django_db
def test_get_product_list_api():
    # Crear productos de prueba
    Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    Producto.objects.create(codigo=2, marca= 'Prueba' , nombre='Producto 2', precio=20.0, stock=200)
    
    # Crear un cliente de API y realizar la solicitud GET para obtener la lista de productos
    client = APIClient()
    response = client.get('/productos/')
    
    # Verificar que la respuesta es 200 OK
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_product_detail_api():
    # Crear un producto de prueba
    Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    
    # Crear un cliente de API y realizar la solicitud GET para obtener el detalle del producto
    client = APIClient()
    response = client.get(f'/productos/1/')
    
    # Verificar que la respuesta es 200 OK
    assert response.status_code == 200
    assert response.data['codigo'] == 1

@pytest.mark.django_db
def test_delete_product_api():
    # Crear un usuario administrador y autenticarlo
    user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')
    
    # Crear un producto de prueba
    producto = Producto.objects.create(codigo=1, marca= 'Prueba' , nombre='Producto 1', precio=10.0, stock=100)
    
    # Realizar la solicitud DELETE para eliminar el producto
    response = client.delete(f'/api/products/{producto.codigo}/')
    
    # Verificar que la respuesta es 204 No Content
    assert response.status_code == 204
    assert Producto.objects.filter(id=producto.id).count() == 0
