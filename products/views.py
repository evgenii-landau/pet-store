from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, ListView, TemplateView

from .models import Basket, BasketItem, Product, ProductCategory


class Index(TemplateView):
    """Отображение главной страницы"""

    template_name = "products/index.html"
    extra_context = {
        "title": "Dapper",
    }


class ProductListView(ListView):
    """Отображение продуктов

    Args:
        category_slug (str) : slug selected category
    """

    model = Product
    template_name = "products/products.html"
    context_object_name = "products"
    slug_url_kwargs = "category_slug"

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwargs)
        if category_slug:
            return Product.objects.filter(cat__slug=category_slug)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dapper"
        context["categories"] = get_list_or_404(ProductCategory)
        return context


class BasketListView(LoginRequiredMixin, ListView):
    """Отображение товаров корзины"""

    model = Basket
    template_name = "products/basket.html"
    context_object_name = "basket_items"

    def get_queryset(self):
        user = self.request.user
        self.basket = Basket.objects.filter(user=user).first()
        if self.basket:
            self.basket_items = self.basket.get_all_items()
        else:
            self.bakset_items = []
        return self.basket_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.basket_items:
            context["total_price"] = self.basket.get_total_price()
            context["count_items"] = sum(item.quantity for item in self.basket_items)
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
        product = get_object_or_404(Product, pk=product_id)
        basket, created = Basket.objects.get_or_create(user=user)

        basket_item, item_created = BasketItem.objects.get_or_create(
            basket=basket,
            product=product,
            defaults={"quantity": 1},
        )

        if not item_created:
            basket_item.quantity += 1
            basket_item.save()

        return redirect("products:products")

    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #     product_id = self.kwargs["product_id"]
    #     product = get_object_or_404(Product, pk=product_id)
    #     basket, created = Basket.objects.get_or_create(user=user)

    #     basket_items, item_created = BasketItem.objects.get_or_create(
    #         basket=basket, product=product
    #     )

    #     if not item_created:
    #         basket_items.quantity += 1
    #         basket_items.save()

    #     return redirect(reverse("products:products"))


class UpdateBasketItemQuntityView(LoginRequiredMixin, View):
    """Обновление количества продукта в корзине"""

    def post(self, request, *args, **kwargs):
        basket_item_id = request.POST.get("basket_item_id")
        quantity = request.POST.get("quantity")

        try:
            quantity = int(quantity)
            basket_item = BasketItem.objects.get(pk=basket_item_id)

            if quantity > 0:
                basket_item.quantity = quantity
                basket_item.save()
                messages.success(request, "Количество товаров было успешно обновлено")
            else:
                basket_item.delete()
                messages.success(request, "Товар удален из корзины")

        except (BasketItem.DoesNotExist, ValueError):
            messages.error(request, "Ошибка при обновлении товара в корзине.")

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
        basket_item = get_object_or_404(BasketItem, pk=basket_item_id)
        return basket_item

    def delete(self, request, *args, **kwargs):
        basket_item = self.get_object()
        product_name = basket_item.product.name
        basket_item.delete()
        messages.success(request, f"Товар {product_name} был успешно удален из корзины")
        return JsonResponse({"success": True})
