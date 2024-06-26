from django.contrib import admin

from .models import Product, ProductCategory, ProductGender


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
    fields = [
        ("name", "quantity"),
        "description",
        "price",
        "cat",
        "basket",
        "image",
        "gend",
    ]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductGender)
class ProductGenderAdmin(admin.ModelAdmin):
    list_display = ["gender", "slug"]
    prepopulated_fields = {"slug": ("gender",)}
