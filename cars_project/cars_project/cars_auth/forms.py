from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from cars_project.core.forms import BootstrapFormMixin

UserModel = get_user_model()


class RegisterForm(BootstrapFormMixin ,UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'age', 'profile_photo')

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise ValidationError('You should have eighteen years to register on this site!')
        return self.cleaned_data['age']


class LoginForm(forms.Form):
    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }

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

    # def clean_password(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #
    #     user = authenticate(email=email, password=password)
    #
    #     if not user:
    #         raise ValidationError(
    #             'Email and/or password is incorrect.'
    #         )
    #
    #     return user


    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise ValidationError(
                'Email and/or password is incorrect.'
            )

        return self.cleaned_data

