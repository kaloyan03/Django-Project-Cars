# Generated by Django 4.0.1 on 2022-01-24 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='user_id',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]