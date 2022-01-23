from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')


class LoginForm(forms.Form):
    # attrs={'class': 'form-control', 'id': 'email'}
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'login-page-input'}
        )
    )

    # attrs={'class':'form-control', 'id': 'password'}
    password = forms.CharField(
        max_length=300,
        widget=forms.PasswordInput(
            attrs={'class': 'login-page-input'}
        )
    )
