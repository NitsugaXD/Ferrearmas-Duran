import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status

@pytest.mark.django_db
def test_user_registration():
    """
    Esta prueba verificar que el registro de usuario sea exitoso.
    """
    client = APIClient()
    response = client.post('/users/', {
        'username': 'testuser',
        'password': 'testpass'
    }, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data

@pytest.mark.django_db
def test_get_user_detail():
    """
    Esta prueba verificar que se pueda obtener el detalle de un usuario registrado.
    """
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    client = APIClient()
    response = client.get(f'/users/view/{user.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == 'testuser'

@pytest.mark.django_db
def test_delete_non_existent_user():
    """
    Esta prueba verificar que se devuelva un error cuando se intente v un usuario inexistente.
    """
    client = APIClient()
    response = client.delete('/users/9999/')  # Asumiendo que el usuario con ID 9999 no existe
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
