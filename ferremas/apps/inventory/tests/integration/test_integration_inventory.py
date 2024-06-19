import pytest
from rest_framework.test import APIClient
from apps.products.models import Producto

# Prueba de integración para la vista InventoryView
@pytest.mark.django_db
def test_inventory_view_get():
    """
    Verifica que la vista InventoryView devuelva correctamente la lista de productos.
    """
    Producto.objects.create(nombre='Test Product 1', precio=100.00, codigo=1,marca='Prueba', stock=10)
    Producto.objects.create(nombre='Test Product 2', precio=200.00, codigo=2,marca='Prueba', stock=10)
    Producto.objects.create(nombre='Test Product 3', precio=300.00, codigo=3,marca='Prueba', stock=10)

    client = APIClient()
    response = client.get('/inventory/')

    assert response.status_code == 200
    assert len(response.data) == 3
