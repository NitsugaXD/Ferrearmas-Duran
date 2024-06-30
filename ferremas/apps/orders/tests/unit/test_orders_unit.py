import pytest
from django.contrib.auth.models import User
from apps.orders.models import Orden
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_create_order_success():
    """Valida la creación exitosa de una orden."""
    user = User.objects.create_user(username='testuser', password='testpassword')
    order = Orden.objects.create(usuario=user, total=100.0, estado='PENDIENTE')
    assert order.usuario.username == 'testuser'
    assert order.total == 100.0
    assert order.estado == 'PENDIENTE'

@pytest.mark.django_db
def test_update_order_status():
    """Valida la actualización del estado de una orden."""
    user = User.objects.create_user(username='testuser', password='testpassword')
    order = Orden.objects.create(usuario=user, total=100.0, estado='PENDIENTE')
    order.estado = 'COMPLETADO'
    order.save()
    updated_order = Orden.objects.get(id=order.id)
    assert updated_order.estado == 'COMPLETADO'


