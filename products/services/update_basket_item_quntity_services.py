from typing import Literal, Union


def update_basket_item_quantity(basket_item: object, quantity: int) -> Union[
    tuple[Literal[True], Literal["Количество товаров было успешно обновлено"]],
    tuple[Literal[True], Literal["Товар удален из корзины"]],
    tuple[Literal[False], Literal["Ошибка при обновлении товара в корзине."]],
]:
    """Обновление количества элемента корзины или его удаление

    Args:
        basket_item (object): элемент корзины
        quantity (int): количество элемнета в корзине

    Returns:
        tuple: Кортеж, содержащий два элемента:
            - bool: Результат операции ('True' в случае успешного обновления или удаления, 'False' в случае ошибки)
            - str: Сообщение об операции (описание результата операции: успешное обновление количества, успешное удаление из корзины или сообщение об ошибке)
    """

    try:
        quantity = int(quantity)
        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
            return True, "Количество товаров было успешно обновлено"
        else:
            basket_item.delete()
            return True, "Товар удален из корзины"
    except ValueError:
        return False, "Ошибка при обновлении товара в корзине."
