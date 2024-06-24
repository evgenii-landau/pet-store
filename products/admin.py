from django.contrib import admin

from .models import Product, ProductCategory


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
    ordering = ["name"]
    list_per_page = 10
    fields = [("name", "quantity"), "description", "price", "cat", "basket", "image"]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "slug"]
    prepopulated_fields = {"slug": ("name",)}
