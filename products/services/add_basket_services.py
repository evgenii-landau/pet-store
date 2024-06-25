from django.shortcuts import get_object_or_404

from products.models import Basket, BasketItem, Product


def get_product_by_product_id(product_id: int) -> Product:
    """Получение продкута по его id

    Args:
        product_id (int): id продукта

    Returns:
        object | Error 404: Возвращает объект продукта
    """

    return get_object_or_404(Product, pk=product_id)


def get_or_create_basket_by_user(user: object) -> tuple[Basket, bool]:
    """Получение корзины по пользователю
    или ее создание для него, если ее нет

    Args:
        user (obj): Объект пользователя

    Returns:
        object: Возвращает кортеж из объекта корзины и булевого значения
    """

    return Basket.objects.get_or_create(user=user)


def get_or_create_basket_item(basket: object, product: object) -> tuple[BasketItem, bool]:
    """Получение элемента корзины если он есть
    или его создание, если его нет

    Args:
        basket (obj): Объект корзины
        product (obj): Объект продукта

    Returns:
        obj: Возвращает кортеж из объекта элемента корзины и булевого значения
    """

    return BasketItem.objects.get_or_create(
        basket=basket,
        product=product,
        defaults={"quantity": 1},
    )
