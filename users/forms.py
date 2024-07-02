import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    """
    Форма для авторизации пользователя
    """

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
    """
    Форма для регистрации пользователя
    """

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
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class ProfileUpdateForm(forms.ModelForm):
    """
    Форма обновления данных профиля пользователя
    """

    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "email", "image")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not re.match(r"^[a-zA-Z]+$", first_name):
            raise forms.ValidationError("The name must contain only characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not re.match(r"^[a-zA-Z]+$", last_name):
            raise forms.ValidationError(
                "The last name must consist of characters only."
            )
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not re.match(r"^[a-zA-Z0-9.@+-]+$", username) or len(username) < 3:
            raise forms.ValidationError(
                "The username must consist only of characters, numbers, @/./+/-//_ symbols, and be longer than 5 in length."
            )
        if (
            get_user_model()
            .objects.exclude(pk=self.instance.pk)
            .filter(username=username)
            .exists()
        ):
            raise forms.ValidationError("A user with this name already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise forms.ValidationError("Enter the correct e-mail address.")
        if (
            get_user_model()
            .objects.exclude(pk=self.instance.pk)
            .filter(email=email)
            .exists()
        ):
            raise forms.ValidationError(
                "A user with this email address already exists."
            )
        return email

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > 5 * 1024 * 1024:  # 5 MB
            raise forms.ValidationError("The image size should not exceed 5 MB.")
        return image
