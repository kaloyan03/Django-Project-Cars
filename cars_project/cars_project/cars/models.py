from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


UserModel = get_user_model()

# Create your models here.
class Car(models.Model):
    vehicle_choices = (
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Motorhomes Or caravanas', 'Motorhomes & Caravanas'),
        ('Trucks', 'Trucks'),
    )

    fuel_choices = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Other', 'Other'),
    )

    transmission_choices = (
        ('Automatic', 'Automatic transmission'),
        ('Manual_gearbox', 'Manual'),
        ('Semi-automatic', 'Semi-automatic'),

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

    price = models.IntegerField(
        default=0
    )

    mileage = models.IntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to='car_photos',
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        default=5,
    )


class Comment(models.Model):
    message = models.TextField()
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        default=5,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        default=5,
    )


class Like(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )