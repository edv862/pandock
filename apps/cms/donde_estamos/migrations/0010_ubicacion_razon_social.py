# Generated by Django 2.0.6 on 2018-08-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donde_estamos', '0009_auto_20180814_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='razon_social',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]