from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'product/products.html')


def product_detail(request, product_slug):
    return render(request, 'product/product_detail.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
