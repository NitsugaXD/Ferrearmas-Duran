from django.urls import include, path
from .views import product_list

urlpatterns = [
    path('productos/', product_list, name='product_list'),
    path('users/', include('apps.users.urls')),
    path('products/', include('apps.products.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('payments/', include('apps.payments.urls')),
    path('inventory/', include('apps.inventory.urls')),
]
