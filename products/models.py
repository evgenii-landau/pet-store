from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество товаров")
    image = models.ImageField(
        upload_to="products_images", db_index=True, verbose_name="Изображение"
    )
    cat = models.ForeignKey(
        to="ProductCategory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
        related_name="products",
        verbose_name="Категория",
    )
    basket = models.ForeignKey(
        to="Basket",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="products",
        verbose_name="Корзина",
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"Продукт: {self.name} | Категория: {self.cat.name}"


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Корзина пользователя: {self.user.username}"

    class Meta:
        db_table = "basket"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class BasketItem(models.Model):
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "basket_item"
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
