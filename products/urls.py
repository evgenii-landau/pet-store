from django.urls import path

from .views import (
    AddBasketView,
    BasketListView,
    DeleteBasketItem,
    Index,
    ProductListView,
    UpdateBasketItemQuantityView,
)

app_name = "products"



urlpatterns = [
	path("", Index.as_view(), name="home"),
	path("products/<slug:category_slug>/", ProductListView.as_view(), name="product_list"),
    # path("<slug:category_slug>/", ProductListView.as_view(), name="category_products"),
    path("<slug:gender_slug>/<slug:category_slug>/", ProductListView.as_view(), name="gender_category_products"),
]

