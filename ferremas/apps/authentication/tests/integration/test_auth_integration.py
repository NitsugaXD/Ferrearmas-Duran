import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from collections.abc import Sequence

@pytest.mark.django_db
def test_custom_auth_token_success():
    """
    Esta prueba valida que el endpoint de autenticación token funcione correctamente con credenciales válidas.
    """
    # Crear un usuario de prueba con el username 'testuser', password 'testpass' y email 'test@example.com'
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')

    # Crear un cliente de la API para realizar solicitudes
    client = APIClient()
    
    # Obtener la URL del endpoint 'custom_auth_token'
    url = reverse('custom_auth_token')
    
    # Datos de la solicitud con credenciales válidas
    data = {'username': 'testuser', 'password': 'testpass'}

    # Realizar una solicitud POST al endpoint con los datos proporcionados
    response = client.post(url, data, format='json')

    # Verificar que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200
    
    # Verificar que la respuesta contenga un token
    assert 'token' in response.data
    
    # Verificar que la respuesta contenga el ID del usuario correcto
    assert response.data['user_id'] == user.id
    
    # Verificar que la respuesta contenga el email del usuario correcto
    assert response.data['email'] == user.email

@pytest.mark.django_db
def test_custom_auth_token_invalid_credentials():
    """
    Esta prueba valida que el endpoint de autenticación token responda con un error cuando se proporcionan credenciales inválidas.
    """
    # Crear un cliente de la API para realizar solicitudes
    client = APIClient()
    
    # Obtener la URL del endpoint 'custom_auth_token'
    url = reverse('custom_auth_token')
    
    # Datos de la solicitud con credenciales inválidas
    data = {'username': 'invaliduser', 'password': 'invalidpass'}

    # Realizar una solicitud POST al endpoint con los datos proporcionados
    response = client.post(url, data, format='json')

    # Verificar que la respuesta tenga un código de estado 400 (Bad Request)
    assert response.status_code == 400
    
    # Verificar que la respuesta contenga un error de campo no válido
    assert 'non_field_errors' in response.data

@pytest.mark.django_db
def test_custom_auth_token_missing_fields():
    """
    Esta prueba valida que el endpoint de autenticación token responda con un error cuando faltan campos requeridos en la solicitud.
    """
    # Crear un cliente de la API para realizar solicitudes
    client = APIClient()
    
    # Obtener la URL del endpoint 'custom_auth_token'
    url = reverse('custom_auth_token')
    
    # Datos de la solicitud con campos faltantes (falta la contraseña)
    data = {'username': 'testuser'}

    # Realizar una solicitud POST al endpoint con los datos proporcionados
    response = client.post(url, data, format='json')

    # Verificar que la respuesta tenga un código de estado 400 (Bad Request)
    assert response.status_code == 400
    
    # Verificar que la respuesta contenga un error indicando que falta la contraseña
    assert 'password' in response.data
