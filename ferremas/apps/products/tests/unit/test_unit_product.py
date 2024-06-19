import pytest
from apps.products.models import Producto

@pytest.mark.django_db
def test_create_product():
    producto = Producto.objects.create(codigo='1234', nombre='Test Product', precio=10.0, stock=100)
    assert producto.codigo == '1234'
    assert producto.nombre == 'Test Product'
    assert producto.precio == 10.0
    assert producto.stock == 100

@pytest.mark.django_db
def test_update_product():
    producto = Producto.objects.create(codigo='1234', nombre='Test Product', precio=10.0, stock=100)
    producto.nombre = 'Updated Product'
    producto.precio = 15.0
    producto.save()

    updated_producto = Producto.objects.get(codigo='1234')
    assert updated_producto.nombre == 'Updated Product'
    assert updated_producto.precio == 15.0

@pytest.mark.django_db
def test_delete_product():
    producto = Producto.objects.create(codigo='1234', nombre='Test Product', precio=10.0, stock=100)
    producto_id = producto.id
    producto.delete()

    with pytest.raises(Producto.DoesNotExist):
        Producto.objects.get(id=producto_id)
