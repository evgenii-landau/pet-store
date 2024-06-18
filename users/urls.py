from django.urls import path
from .views import LoginUser, register_user

app_name = "users"


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", register_user, name="register"),
]
