from django.shortcuts import render

def product_form(request):
    return render(request, 'product_form.html')


def product_list_view(request):
    return render(request, 'product_list.html')

def update_product_form(request):
    return render(request, 'update_product.html')