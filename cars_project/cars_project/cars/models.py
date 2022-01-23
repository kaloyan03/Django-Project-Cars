from django.db import models

# Create your models here.
class Car(models.Model):
    vehicle_choices = (
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('motorhomes_or_caravanas', 'Motorhomes & Caravanas'),
        ('trucks', 'Trucks'),
    )

    fuel_choices = (
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('other', 'Other'),
    )

    transmission_choices = (
        ('automatic', 'Automatic transmission'),
        ('manual_gearbox', 'Manual'),
        ('semi-automatic', 'Semi-automatic'),

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

    image = models.ImageField(
        upload_to='car_photos',
        null=True,
    )

