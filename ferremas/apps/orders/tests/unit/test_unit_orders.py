import pytest
from django.contrib.auth import get_user_model
from apps.products.models import Producto
from apps.orders.models import Pedido , PedidoProducto
User = get_user_model()

# Prueba unitaria para la creación de una instancia de Pedido
@pytest.mark.django_db
def test_create_pedido():
    """
    Verifica que se pueda crear una instancia de Pedido.
    """
    user = User.objects.create_user(username='testuser', password='testpass')
    pedido = Pedido.objects.create(usuario=user, total=100.00, pagado=True)
    assert pedido.usuario == user
    assert pedido.total == 100.00
    assert pedido.pagado == True

# Prueba unitaria para añadir productos a un pedido
@pytest.mark.django_db
def test_add_producto_to_pedido():
    """
    Verifica que se puedan añadir productos a un pedido.
    """
    user = User.objects.create_user(username='testuser', password='testpass')
    pedido = Pedido.objects.create(usuario=user, total=100.00, pagado=True)
    producto = Producto.objects.create(nombre='Test Product', precio=100.00, codigo=1, stock=20)
    pedido_producto = PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=2)
    
    assert pedido.productos.count() == 1
    assert pedido_producto.producto == producto
    assert pedido_producto.cantidad == 2
