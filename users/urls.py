from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginUser, RegisterUser, profile

app_name = "users"


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
