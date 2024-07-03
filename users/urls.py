from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (
    LoginUser,
    ProfileChangePasswordView,
    ProfileUpdateView,
    ProfileView,
    RegisterUser,
)

app_name = "users"


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/details/", ProfileUpdateView.as_view(), name="profile_details"),
    path(
        "profile/change_password/",
        ProfileChangePasswordView.as_view(),
        name="profile_change_password",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
