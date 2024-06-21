from django.urls import path

from .views import add_basket, basket, products

app_name = "products"


urlpatterns = [
    path("", products, name="products"),
    path("basket/", basket, name="basket"),
    path("basket/add/<int:product_id>/", add_basket, name="add_basket"),
]
