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
        related_name="cat",
        verbose_name="Категория",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user",
        verbose_name="Пользователь",
    )
    basket = models.ForeignKey(
        to="Basket",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="basket",
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
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.BooleanField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantity
