# Generated by Django 2.0.6 on 2018-08-11 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0002_auto_20180720_0831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nosotros',
            old_name='columna_uno',
            new_name='descripcion',
        ),
    ]