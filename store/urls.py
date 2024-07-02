from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import (
    AddBasketView,
    BasketListView,
    DeleteBasketItem,
    SearchListView,
    UpdateBasketItemQuantityView,
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("men/", include(("products.urls", "products"), namespace="men")),
    path("women/", include(("products.urls", "products"), namespace="women")),
    path("basket/", BasketListView.as_view(), name="basket"),
    path("basket/add/<int:product_id>/", AddBasketView.as_view(), name="add_basket"),
    path("basket/update_basket_item_quantity/", UpdateBasketItemQuantityView.as_view(), name="update_basket_item_quantity"),
    path("basket/item/<int:pk>/delete/", DeleteBasketItem.as_view(), name="delete_basket_item"),
    path("search/", SearchListView.as_view(), name="search"),
    path("users/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Администрирование сайта"
