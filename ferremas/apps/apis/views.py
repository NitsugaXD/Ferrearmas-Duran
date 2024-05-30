from django.shortcuts import render
from apps.products.models import Producto


def product_list(request):
    productos = Producto.objects.all()
    return render(request, 'product_list.html', {'productos': productos})

