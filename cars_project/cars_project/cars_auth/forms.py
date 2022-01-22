from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')


class LoginForm(forms.Form):
    email = forms.EmailField(

    )

    password = forms.CharField(
        max_length=300,
        widget=forms.PasswordInput()
    )