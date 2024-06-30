from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(
            attrs={
                "class": "login-form-input",
                "placeholder": "Enter username",
            },
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "login-form-input", "placeholder": "Enter password"}
        ),
    )


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "login-form-input", "placeholder": "Enter name"}
        ),
        label="Name",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "login-form-input", "placeholder": "Enter surname"}
        ),
        label="Surname",
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "login-form-input",
                "placeholder": "Enter username",
            }
        ),
        label="Username",
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "login-form-input",
                "placeholder": "Enter E-mail",
            }
        ),
        label="E-mail",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "login-form-input", "placeholder": "Enter password"}
        ),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "login-form-input", "placeholder": "Repeat password"}
        ),
        label="Repeat password",
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


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4"})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-label"}), required=False
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control py-4", "readonly": True})
    )

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "image", "username", "email"]
