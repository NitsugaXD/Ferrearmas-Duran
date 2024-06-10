from django.urls import include, path
from . import views

urlpatterns = [
    path('crear_producto/', views.product_form, name='product_form'),
    path('lista_productos/', views.product_list_view, name='product_list_view'),
    path('actualizar_producto/', views.update_product_form, name='update_product_form'),
    path('users/', include('apps.users.urls')),
    path('products/', include('apps.products.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('payments/', include('apps.payments.urls')),
    path('inventory/', include('apps.inventory.urls')),
]
