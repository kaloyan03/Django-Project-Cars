from django.contrib.auth import get_user_model
from django.db import models

from cars_project.cars.models import Car

UserModel = get_user_model()


class RentCar(models.Model):
    date_start_rent = models.DateField(
        null=True,
    )

    date_end_rent = models.DateField(
        null=True,
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )


    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
