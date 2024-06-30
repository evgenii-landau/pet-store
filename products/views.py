from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import resolve, reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView, ListView, TemplateView

from products.services.add_basket_services import (
    get_or_create_basket_by_user,
    get_or_create_basket_item,
    get_product_by_product_id,
)
from products.services.basket_list_services import (
    check_the_existance_of_a_cart,
    get_basket_by_user,
    get_total_count_items_in_basket,
)
from products.services.product_list_services import (
    get_all_categories,
    get_products_by_category_slug,
)
from products.services.services import get_basket_item_by_id, get_current_gender
from products.services.update_basket_item_quntity_services import (
    update_basket_item_quantity,
)
from static.vendor.data.brands import brands_data
from static.vendor.data.collages import collages_data
from static.vendor.data.sale import sale_data
from static.vendor.data.slider import slider_data

from .models import Basket, BasketItem, Product


class Index(TemplateView):
    """Отображение главной страницы"""

    template_name = "products/index.html"
    extra_context = {
        "categories": get_all_categories(),
        "slider_data": slider_data,
        "brands_data": brands_data,
        "collages_data": collages_data,
        "sale_data": sale_data,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resolved_path = resolve(self.request.path)
        context["current_gender"] = get_current_gender(resolved_path)
        return context


class ProductListView(ListView):
    """Отображение списка продуктов

    Args:
        category_slug (str) : Слаг выбранной категории
    """

    model = Product
    template_name = "products/products.html"
    context_object_name = "products"
    slug_url_kwargs = "category_slug"
    paginate_by = 12

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwargs)
        resolved_path = resolve(self.request.path)
        current_gender = get_current_gender(resolved_path)
        return get_products_by_category_slug(category_slug, current_gender)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_all_categories()
        return context


class BasketListView(LoginRequiredMixin, ListView):
    """Отображение товаров корзины"""

    model = Basket
    template_name = "products/basket.html"
    context_object_name = "basket_items"

    def get_queryset(self):
        user = self.request.user
        self.basket = get_basket_by_user(user)
        self.basket_items = check_the_existance_of_a_cart(self.basket)
        return self.basket_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.basket_items:
            context["total_price"] = self.basket._get_total_price()
            context["count_items"] = get_total_count_items_in_basket(self.basket_items)
        else:
            context["total_price"] = 0
            context["count_items"] = 0
        return context


class AddBasketView(LoginRequiredMixin, View):
    """Добавление продукта в корзину

    Args:
        product_id (int): id продукта
    """

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = kwargs.get("product_id")
        product = get_product_by_product_id(product_id)
        basket, created = get_or_create_basket_by_user(user)
        basket_item, item_created = get_or_create_basket_item(basket, product)

        if not item_created:
            basket_item.quantity += 1
            basket_item.save()

        return redirect(request.META.get("HTTP_REFERER"))


class UpdateBasketItemQuantityView(LoginRequiredMixin, View):
    """Обновление количества продукта в корзине"""

    def post(self, request, *args, **kwargs):
        basket_item_id = request.POST.get("basket_item_id")
        quantity = request.POST.get("quantity")

        basket_item = get_basket_item_by_id(basket_item_id)
        success, message = update_basket_item_quantity(basket_item, quantity)

        if success:
            messages.success(request, message)
        else:
            messages.error(request, message)

        return redirect("products:basket")


class DeleteBasketItem(LoginRequiredMixin, DeleteView):
    """Удаление продукта из корзины

    Args:
        basket_item_id (int): id продукта
    """

    model = BasketItem
    success_url = reverse_lazy("products:basket")

    def get_object(self, queryset=None):
        basket_item_id = self.kwargs["pk"]
        return get_basket_item_by_id(basket_item_id)

    def delete(self, request, *args, **kwargs):
        basket_item = self.get_object()
        product_name = basket_item.product.name
        basket_item.delete()
        messages.success(request, f"Товар {product_name} был успешно удален из корзины")
        return JsonResponse({"success": True})


# class GenderListView(LoginRequiredMixin, ListView):
#     model = ProductGender
#     template_name = "products/products.html"
#     context_object_name = "genders"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Dapper"
#         context["categories"] = get_all_categories()
#         context["products"] = Product.objects.all()
#         return context
