from django.db import models

# Create your models here.
class Car(models.Model):
    vehicle_choices = (
        ('Car', 'car'),
        ('Motorcycle', 'motorcycle'),
        ('Motorhomes & Caravanas', 'motorhomes_or_caravanas'),
        ('Trucks', 'trucks'),
    )

    fuel_choices = (
        ('Petrol', 'petrol'),
        ('Diesel', 'diesel'),
        ('Electric', 'electric'),
        ('Other', 'other'),
    )

    transmission_choices = (
        ('Automatic transmission', 'automatic'),
        ('Manual gearbox', 'manual'),
        ('Semi-automatic', 'semi-automatic'),

    )


    vehicle_type = models.CharField(
        max_length=50,
        choices=vehicle_choices,
    )

    make = models.CharField(
        max_length=40
    )

    model = models.CharField(
        max_length=40
    )

    fuel_type = models.CharField(
        max_length=15,
        choices=fuel_choices,
    )

    transmission_type = models.CharField(
        max_length=40,
        choices=transmission_choices,
    )

    mileage = models.IntegerField(
        default=0
    )

