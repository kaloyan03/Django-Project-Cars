from django import forms

from cars_project.cars_rent_car.models import RentCar
from cars_project.core.forms import BootstrapFormMixin

class DateInput(forms.DateInput):
    input_type = 'date'


class RentCarForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RentCar
        fields = '__all__'
        exclude = ['user', 'car']
        widgets = {
            'date_start_rent': DateInput(),
            'date_end_rent': DateInput(),
        }
