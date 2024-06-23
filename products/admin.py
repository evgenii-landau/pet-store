from django.contrib import admin

from .models import Basket, Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "price",
        "quantity",
        "image",
        "cat",
        "basket",
    ]
    list_editable = ["price", "quantity", "image", "cat"]
    search_fields = ["name"]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass
