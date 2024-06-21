from django.urls import path

from .views import (
    add_basket,
    basket,
    delete_bakset_item,
    products,
    update_basket_item_quantity,
)

app_name = "products"


urlpatterns = [
    path("", products, name="products"),
    path("basket/", basket, name="basket"),
    path("basket/add/<int:product_id>/", add_basket, name="add_basket"),
    path(
        "basket/update_basket_item_quantity/",
        update_basket_item_quantity,
        name="update_basket_item_quantity",
    ),
    path("basket/delete_bakset_item/", delete_bakset_item, name="delete_bakset_item"),
]
