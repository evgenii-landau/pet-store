from django.urls import path
from .views import LoginUser, RegisterUser, profile

app_name = "users"


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile, name="profile"),
]
