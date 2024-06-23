from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse

from .models import Basket, BasketItem, Product, ProductCategory


def index(request):
    """Отображение главной страницы"""

    context = {
        "title": "Store",
    }
    return render(request, "products/index.html", context=context)


def products(request, category_id):
    """Отображение товаров и категорий"""

	

    context = {
        "title": "Store - Каталог",
        "products": get_list_or_404(Product),
        "categories": get_list_or_404(ProductCategory),
    }
    return render(request, "products/products.html", context=context)


def basket(request):
    """Отображение товаров корзины"""

    user = request.user
    basket = Basket.objects.filter(user=user).first()
    basket_items = basket.get_all_items()
    total_price = basket.get_total_price()
    count_items = sum(item.quantity for item in basket_items)

    context = {
        "basket_items": basket_items,
        "total_price": total_price,
        "count": count_items,
    }

    return render(request, "products/basket.html", context=context)


@login_required
def add_basket(request, product_id):
    """Добавление продукта в корзину

    Args:
        product_id (int): id продукта
    """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    basket, created = Basket.objects.get_or_create(user=user)

    basket_items, item_created = BasketItem.objects.get_or_create(
        basket=basket, product=product
    )

    if not item_created:
        basket_items.quantity += 1
        basket_items.save()

    return redirect(reverse("products:products"))


@login_required
def update_basket_item_quantity(request):
    """Обновление количества продукта в корзине"""

    if request.method == "POST":
        basket_item_id = request.POST.get("basket_item_id")
        quantity = request.POST.get("quantity")

        try:
            quantity = int(quantity)
            basket_item = BasketItem.objects.get(pk=basket_item_id)

            if quantity > 0:
                basket_item.quantity = quantity
                basket_item.save()
                messages.success(request, "Количество товаров было успешно обновлено")
            else:
                basket_item.delete()
                messages.success(request, "Товар удален из корзины")

        except (BasketItem.DoesNotExist, ValueError):
            messages.error(request, "Ошибка при обновлении товара в корзине.")

    return redirect("products:basket")


@login_required
def delete_bakset_item(request, basket_item_id):
    """Удаление продукта из корзины

    Args:
        basket_item_id (int): id продукта
    """

    basket_item = get_object_or_404(BasketItem, pk=basket_item_id)
    product_name = basket_item.product.name
    basket_item.delete()

    messages.success(request, f"Товар {product_name} был успешно удален из корзины")

    return redirect("products:basket")
