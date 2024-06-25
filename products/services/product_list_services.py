from django.shortcuts import get_list_or_404

from products.models import Product, ProductCategory


def get_products_by_category_slug(category_slug: str):
    """Получение продуктов по slug(у) Категории"""

    if category_slug:
        return Product.objects.filter(cat__slug=category_slug)
    return Product.objects.all()


def get_all_categories() -> list[ProductCategory]:
    """Получение всех категорий"""

    return get_list_or_404(ProductCategory)
