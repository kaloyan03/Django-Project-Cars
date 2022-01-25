from django import forms

from cars_project.cars.models import Car
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