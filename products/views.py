from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_list_or_404


def index(request):
    """Отображение главной страницы"""

    context = {
        "title": "Store",
    }
    return render(request, "products/index.html", context=context)


def products(request):
    """Отображение товаров и категорий"""

    context = {
        "title": "Store - Каталог",
        "products": get_list_or_404(Product),
        "categories": get_list_or_404(ProductCategory),
    }
    return render(request, "products/products.html", context=context)
