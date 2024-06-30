from django.urls import path, include
from apps.products import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('view/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('update/<int:pk>/', views.ProductoUpdateView.as_view(), name='producto-update'),
]
