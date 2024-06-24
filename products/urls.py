from django.urls import path, re_path

from .views import (
    ProductListView,
    add_basket,
    basket,
    delete_bakset_item,
    update_basket_item_quantity,
)

app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<slug:category_slug>/", ProductListView.as_view(), name="products"),
    path("basket/", basket, name="basket"),
    path("basket/add/<int:product_id>/", add_basket, name="add_basket"),
    path(
        "basket/update_basket_item_quantity/",
        update_basket_item_quantity,
        name="update_basket_item_quantity",
    ),
    path(
        "basket/delete_bakset_item/<int:basket_item_id>/",
        delete_bakset_item,
        name="delete_bakset_item",
    ),
]
