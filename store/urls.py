from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import Index

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("men/", Index.as_view(), name="home_men"),
    path("women/", Index.as_view(), name="home_women"),
    path("products/", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Администрирование сайта"
