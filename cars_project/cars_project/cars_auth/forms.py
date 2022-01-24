from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from cars_project.core.forms import BootstrapFormMixin

UserModel = get_user_model()


class RegisterForm(BootstrapFormMixin ,UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        max_length=300,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
