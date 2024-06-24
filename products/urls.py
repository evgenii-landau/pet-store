from django.urls import path

from .views import (
    AddBasketView,
    BasketListView,
    ProductListView,
    delete_bakset_item,
    update_basket_item_quantity,
)

app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("basket/", BasketListView.as_view(), name="basket"),
    path("basket/add/<int:product_id>/", AddBasketView.as_view(), name="add_basket"),
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
    path("<slug:category_slug>/", ProductListView.as_view(), name="products"),
]
