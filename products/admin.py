from django.contrib import admin

from .models import Basket, Product, ProductCategory

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
