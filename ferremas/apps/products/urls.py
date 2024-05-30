from django.urls import path
from .views import ProductoListCreate, ProductoRetrieveUpdateDestroy

urlpatterns = [
    path('', ProductoListCreate.as_view(), name='producto-list-create'),
    path('<str:codigo>/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-detail'),
]
