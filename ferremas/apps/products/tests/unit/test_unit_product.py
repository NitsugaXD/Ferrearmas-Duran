import pytest
from apps.products.models import Producto

@pytest.mark.django_db
def test_create_product():
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    assert producto.nombre == 'Producto de prueba'
    assert producto.precio == 10.0
    assert producto.codigo == 1
    assert producto.stock == 100

@pytest.mark.django_db
def test_get_product():
    Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    obtener = Producto.objects.get(codigo=1)
    assert obtener.nombre == 'Producto de prueba'
    assert obtener.precio == 10.0
    assert obtener.codigo == 1
    assert obtener.stock == 100

@pytest.mark.django_db
def test_update_product_stock():
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    producto.stock = 50
    producto.save()
    assert producto.stock == 50

@pytest.mark.django_db
def test_delete_product():
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    producto.delete()
    assert not Producto.objects.filter(codigo=1).exists()
