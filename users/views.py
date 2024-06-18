from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy("home")


def register_user(request):
    context = {}
    return render(request, "users/register.html", context=context)
