# Generated by Django 2.0.6 on 2018-08-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donde_estamos', '0010_ubicacion_razon_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='mapa_url',
            field=models.URLField(max_length=1000),
        ),
    ]
