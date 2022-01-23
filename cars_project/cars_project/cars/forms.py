from django import forms

from cars_project.cars.models import Car


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
        }