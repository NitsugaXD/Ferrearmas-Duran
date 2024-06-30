import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_update_user():
    user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
    user.username = 'updateduser'
    user.email = 'updateduser@example.com'
    user.save()
    updated_user = User.objects.get(id=user.id)
    assert updated_user.username == 'updateduser'
    assert updated_user.email == 'updateduser@example.com'


@pytest.mark.django_db
def test_delete_user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    user_id = user.id
    user.delete()
    with pytest.raises(User.DoesNotExist):
        User.objects.get(id=user_id)
