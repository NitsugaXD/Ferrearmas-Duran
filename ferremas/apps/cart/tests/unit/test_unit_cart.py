import pytest
from django.contrib.auth.models import User
from apps.products.models import Producto
from apps.cart.models import Carro, CarroProducto  

@pytest.mark.django_db
class TestCarroModel:
    def test_create_carro(self):
        """
        Esta prueba verifica que se pueda crear un objeto Carro correctamente.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        carro = Carro.objects.create(usuario=user)

        assert carro.usuario == user
        assert carro.productos.count() == 0
        assert carro.fecha_creacion is not None

@pytest.mark.django_db
class TestCarroProductoModel:
    def test_create_carro_producto(self):
        """
        Esta prueba verifica que se pueda crear una relación CarroProducto correctamente.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        carro = Carro.objects.create(usuario=user)
        producto = Producto.objects.create(nombre='Producto de prueba', precio=10.0, codigo=1, stock=20)
        carro_producto = CarroProducto.objects.create(carro=carro, producto=producto, cantidad=2)

        assert carro_producto.carro == carro
        assert carro_producto.producto == producto
        assert carro_producto.cantidad == 2
