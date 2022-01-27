from django import forms

from cars_project.cars.models import Car, Comment
from cars_project.core.forms import BootstrapFormMixin


class AddCarForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user']


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user', 'transmission_type', 'fuel_type', 'vehicle_type']


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    message = forms.CharField(label='Add comment', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['car', 'user']