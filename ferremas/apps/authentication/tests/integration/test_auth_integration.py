import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_custom_auth_token_success():
    """
    Esta prueba valida que el sistema permita la autenticación con credenciales válidas.
    """
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    client = APIClient()
    url = reverse('custom_auth_token')
    data = {'username': 'testuser', 'password': 'testpass'}
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'token' in response.data

@pytest.mark.django_db
def test_custom_auth_token_invalid_credentials():
    """
    Esta prueba valida que el sistema rechace la autenticación con credenciales inválidas.
    """
    client = APIClient()
    url = reverse('custom_auth_token')
    data = {'username': 'invaliduser', 'password': 'invalidpass'}
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'non_field_errors' in response.data

@pytest.mark.django_db
def test_custom_auth_token_missing_fields():
    """
    Esta prueba valida que el sistema devuelva un error cuando faltan campos requeridos.
    """
    client = APIClient()
    url = reverse('custom_auth_token')
    data = {'username': 'testuser'}
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'password' in response.data


