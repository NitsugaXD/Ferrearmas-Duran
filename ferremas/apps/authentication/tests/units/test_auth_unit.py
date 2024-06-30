import pytest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    assert user.username == 'testuser'
    assert user.check_password('testpassword') is True

@pytest.mark.django_db
def test_create_user_no_username():
    with pytest.raises(ValueError):
        User.objects.create_user(username='', password='testpassword')

@pytest.mark.django_db
def test_authenticate_user():
    User.objects.create_user(username='testuser', password='testpassword')
    authenticated_user = authenticate(username='testuser', password='testpassword')
    assert authenticated_user is not None

@pytest.mark.django_db
def test_authenticate_user_fail():
    User.objects.create_user(username='testuser', password='testpassword')
    authenticated_user = authenticate(username='testuser', password='wrongpassword')
    assert authenticated_user is None
