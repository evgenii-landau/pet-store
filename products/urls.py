from django.urls import path

from .views import (
    AddBasketView,
    BasketListView,
    DeleteBasketItem,
    ProductListView,
    UpdateBasketItemQuantityView,
)

app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("basket/", BasketListView.as_view(), name="basket"),
    path("basket/add/<int:product_id>/", AddBasketView.as_view(), name="add_basket"),
    path(
        "basket/update_basket_item_quantity/",
        UpdateBasketItemQuantityView.as_view(),
        name="update_basket_item_quantity",
    ),
    path(
        "basket/item/<int:pk>/delete/",
        DeleteBasketItem.as_view(),
        name="delete_basket_item",
    ),
    path("<slug:gender_slug>/", ProductListView.as_view(), name="products"),
    path("<slug:gender_slug>/<slug:category_slug>/", ProductListView.as_view(), name="products"),
]

# /products/
# /products/man/
# /products/man/shoes/
