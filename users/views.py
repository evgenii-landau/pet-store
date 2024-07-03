from webbrowser import get

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from static.vendor.data.static_data import profile_data

from .forms import (
    ProfileUpdateForm,
    ProfileUpdatePasswordForm,
    UserLoginForm,
    UserRegisterForm,
)


class LoginUser(LoginView):
    """Класс представления для авторизации пользователя"""

    form_class = UserLoginForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("men:home")


class RegisterUser(CreateView):
    """Класс представления для регистрация пользователя"""

    form_class = UserRegisterForm
    template_name = "users/register.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("users:login")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Вы успешно зарегистрированы!")
        return super().form_valid(form)


class ProfileView(TemplateView):
    """Класс представления для отображения профиля пользователя"""

    template_name = "users/profile.html"
    extra_context = {"profile_data": profile_data}


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Класс представления для обновления профиля пользователя"""

    form_class = ProfileUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile_details")

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_data"] = profile_data
        return context


class ProfileChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    """Класс представления для обновления пароля пользователя"""

    form_class = ProfileUpdatePasswordForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile_change_password")
    extra_context = {"profile_data": profile_data}
