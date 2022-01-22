# Generated by Django 4.0.1 on 2022-01-22 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)])),
                ('profile_photo', models.ImageField(default='default.jpg', upload_to='profile_photos')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]