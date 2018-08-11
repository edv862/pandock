# Generated by Django 2.0.6 on 2018-07-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20180720_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='productos/pdf'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/producto'),
        ),
    ]
