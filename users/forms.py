from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            },
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите пароль"}
        ),
    )


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите имя"}
        ),
        label="Имя",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите фамилию"}
        ),
        label="Фамилия",
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        ),
        label="Имя пользователя",
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите адрес эл. почты",
            }
        ),
        label="E-mail",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите пароль"}
        ),
        label="Пароль",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Подтвердите пароль"}
        ),
        label="Подтверждение пароля",
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
