from django.shortcuts import render, redirect

def product_form(request):
    return render(request, 'product_form.html')

def product_list_view(request):
    return render(request, 'product_list.html')

def update_product_form(request):
    return render(request, 'update_product.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def products_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'products.html')
