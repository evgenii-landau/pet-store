from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse

from .models import Basket, BasketItem, Product, ProductCategory


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


def basket(request):
    user = request.user
    basket = Basket.objects.filter(user=user).first()

    if basket:
        basket_items = basket.items.all().select_related("product")
        total_price = basket_items.aggregate(total=Sum("total_price"))["total"] or 0
        context = {
            "basket_items": basket_items,
            "count": basket_items.count(),
            "total": total_price,
        }
    else:
        context = {
            "basket_items": [],
            "count": 0,
            "total": 0,
        }

    return render(request, "products/basket.html", context=context)


def add_basket(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    basket, created = Basket.objects.get_or_create(user=user)

    basket_items, item_created = BasketItem.objects.get_or_create(
        basket=basket, product=product, defaults={"total_price": product.price}
    )

    if not item_created:
        basket_items.quantity += 1
        basket_items.total_price += product.price
        basket_items.save()

    return redirect(reverse("products:basket"))
