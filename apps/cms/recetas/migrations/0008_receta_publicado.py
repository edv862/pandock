# Generated by Django 2.0.6 on 2018-08-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0007_auto_20180811_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
