# Generated by Django 4.0.1 on 2022-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_fuel_type_alter_car_transmission_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='car_photos'),
        ),
    ]
