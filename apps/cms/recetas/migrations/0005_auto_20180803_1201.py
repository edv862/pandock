# Generated by Django 2.0.6 on 2018-08-03 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_auto_20180803_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receta',
            options={'ordering': ['titulo']},
        ),
    ]