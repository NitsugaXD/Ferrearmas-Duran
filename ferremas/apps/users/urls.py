from django.urls import path
from .views import RegisterView, UserDetailView, UserDeleteView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('view/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
