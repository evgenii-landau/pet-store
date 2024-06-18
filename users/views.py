from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("home")


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("users:login")
