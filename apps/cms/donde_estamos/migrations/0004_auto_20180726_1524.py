# Generated by Django 2.0.6 on 2018-07-26 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donde_estamos', '0003_ubicacionmapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacionmapa',
            name='x_coord',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Coordenada X'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ubicacionmapa',
            name='y_coord',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Coordenada X'),
            preserve_default=False,
        ),
    ]
