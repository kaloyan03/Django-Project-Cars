from django import forms
from django.core.exceptions import ValidationError

from cars_project.cars.models import Car, Comment
from cars_project.core.forms import BootstrapFormMixin


class AddCarForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user']

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise ValidationError('Price cannot be negative or null.')

        return self.cleaned_data['price']

    def clean_mileage(self):
        mileage = self.cleaned_data.get('mileage')

        if mileage <= 0:
            raise ValidationError('Mileage cannot be negative or null.')

        return self.cleaned_data['mileage']


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user', 'transmission_type', 'fuel_type', 'vehicle_type']

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise ValidationError('Price cannot be negative or null.')

        return self.cleaned_data['price']

    def clean_mileage(self):
        mileage = self.cleaned_data.get('mileage')

        if mileage <= 0:
            raise ValidationError('Mileage cannot be negative or null.')

        return self.cleaned_data['mileage']


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    message = forms.CharField(label='Add comment', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['car', 'user']