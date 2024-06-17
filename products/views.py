from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_list_or_404


def index(request):
    context = {
        "title": "Store",
    }
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": get_list_or_404(Product),
        "categories": get_list_or_404(ProductCategory),
    }
    return render(request, "products/products.html", context=context)
