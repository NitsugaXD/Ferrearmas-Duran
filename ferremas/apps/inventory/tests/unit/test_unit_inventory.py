import pytest
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, MagicMock
from inventory.views import InventoryView

# Prueba unitaria para la vista InventoryView
@pytest.mark.django_db
@patch('inventory.views.Producto')
@patch('inventory.views.ProductoSerializer')
def test_inventory_view_get(mock_serializer_class, mock_producto):
    """
    Verifica que la vista InventoryView devuelva correctamente la lista de productos.
    """
    # Crear un mock para el queryset de productos
    mock_producto.objects.all.return_value = [MagicMock() for _ in range(3)]
    mock_serializer = MagicMock()
    mock_serializer.data = [{'id': 1, 'nombre': 'Test Product 1'}, {'id': 2, 'nombre': 'Test Product 2'}, {'id': 3, 'nombre': 'Test Product 3'}]
    mock_serializer_class.return_value = mock_serializer

    factory = APIRequestFactory()
    view = InventoryView.as_view()
    request = factory.get('/inventory/')
    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 3
