from django.shortcuts import get_object_or_404

from products.models import BasketItem

# common services


def get_basket_item_by_id(pk: int) -> BasketItem:
    """Получение объекта корзина по pk

    Args:
        pk (int): pk элемента

    Returns:
        BasketItem: объекта корзины
    """

    return get_object_or_404(BasketItem, pk=pk)
