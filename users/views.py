from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import UserLoginForm, UserProfileForm, UserRegisterForm


class LoginUser(LoginView):
    """Авторизация пользователя"""

    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("home")


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


def profile(request):
    """Функция для обновления профиля"""

    if request.method == "POST":
        form = UserProfileForm(
            instance=request.user, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {"title": "Store - Профиль", "form": form}
    return render(request, "users/profile.html", context=context)
