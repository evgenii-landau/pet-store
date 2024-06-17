from django.db import models


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

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.cat.name}'


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     date_update = models.DateField(auto_now=True, verbose_name="Дата обновления")
#     slug = models.SlugField(
#         max_length=150,
#         unique=True,
#         db_index=True,
#         blank=True,
#         null=True,
#         verbose_name="URL",
#     )

# slug = models.SlugField(max_length=150, unique=True, db_index=True)
