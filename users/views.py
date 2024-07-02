from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from static.vendor.data.static_data import profile_data

from .forms import ProfileUpdateForm, UserLoginForm, UserRegisterForm


class LoginUser(LoginView):
    """Авторизация пользователя"""

    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("men:home")


class RegisterUser(CreateView):
    """Регистрация пользователя"""

    form_class = UserRegisterForm
    template_name = "users/register.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("users:login")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Вы успешно зарегистрированы!")
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение данных пользователя"""

    form_class = ProfileUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_data"] = profile_data
        return context
