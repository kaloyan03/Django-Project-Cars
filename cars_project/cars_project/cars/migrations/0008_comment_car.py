# Generated by Django 4.0.1 on 2022-01-27 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
    ]