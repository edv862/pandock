# Generated by Django 2.0.6 on 2018-08-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_receta_complejidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='complejidad',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]