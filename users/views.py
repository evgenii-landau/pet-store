from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse


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


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {"title": "Store - Профиль", "form": form}
    return render(request, "users/profile.html", context=context)
