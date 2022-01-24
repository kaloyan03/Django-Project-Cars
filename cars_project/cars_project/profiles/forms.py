from django import forms
from django.contrib.auth import get_user_model

from cars_project.core.forms import BootstrapFormMixin

UserModel = get_user_model()

class ChangeProfilePhotoForm(BootstrapFormMixin ,forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['profile_photo']

