import pytest
from django.contrib.auth.models import User
from apps.cart.models import Carro, CarroProducto
from apps.products.models import Producto

@pytest.mark.django_db
def test_add_product_to_cart():
    user = User.objects.create_user(username='testuser', password='testpassword')
    carrito = Carro.objects.create(usuario=user)
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    carro_producto = CarroProducto.objects.create(carro=carrito, producto=producto, cantidad=2)
    assert carro_producto.producto.codigo == 1
    assert carro_producto.producto.nombre == 'Producto de prueba'

@pytest.mark.django_db
def test_remove_product_from_cart():
    user = User.objects.create_user(username='testuser', password='testpassword')
    carrito = Carro.objects.create(usuario=user)
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    carro_producto = CarroProducto.objects.create(carro=carrito, producto=producto, cantidad=2)
    carro_producto.delete()
    assert carrito.productos.count() == 0

@pytest.mark.django_db
def test_update_product_quantity_in_cart():
    user = User.objects.create_user(username='testuser', password='testpassword')
    carrito = Carro.objects.create(usuario=user)
    producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=100)
    carro_producto = CarroProducto.objects.create(carro=carrito, producto=producto, cantidad=2)
    carro_producto.cantidad = 5
    carro_producto.save()
    assert carro_producto.cantidad == 5

@pytest.mark.django_db
def test_calculate_cart_total():
    user = User.objects.create_user(username='testuser', password='testpassword')
    carrito = Carro.objects.create(usuario=user)
    producto1 = Producto.objects.create(nombre='Producto 1', precio=10.0, codigo=1, stock=100)
    producto2 = Producto.objects.create(nombre='Producto 2', precio=20.0, codigo=2, stock=100)
    CarroProducto.objects.create(carro=carrito, producto=producto1, cantidad=2)
    CarroProducto.objects.create(carro=carrito, producto=producto2, cantidad=1)
    total = sum(item.producto.precio * item.cantidad for item in CarroProducto.objects.filter(carro=carrito))
    assert total == 40.0
