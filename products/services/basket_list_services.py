


from typing import List, Union
from django.db.models import QuerySet

from products.models import Basket


def get_basket_by_user(user) -> Basket | None:
    """Получение корзины пользователя

    Args:
        user (User): объект пользователя

    Returns:
        Basket: объект корзины или None, если корзина не найдена
    """
    return Basket.objects.filter(user=user).first()


def get_total_count_items_in_basket(basket_items: list) -> int:
    """Получение общего количества элементов в корзине

    Args:
        basket_items (list): Список всех элементов в корзине

    Returns:
        total: Сумма всех элемнетов корзины
    """

    return sum(item.quantity for item in basket_items)


def check_the_existance_of_a_cart(basket: Union[Basket, None]) -> List:
    """Проверка на существование корзины

    Args:
        basket (obj or None): Корзина или None

    Returns:
        list: Список элемнетов корзины, если она есть, либо пустой список.
    """

    if basket:
        return basket._get_all_items()
    return []
