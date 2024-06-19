from django.urls import path, include
from apps.products import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
]
