from django.contrib import admin

# Register your models here.
from cars_project.cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model']

admin.site.register(Car, CarAdmin)