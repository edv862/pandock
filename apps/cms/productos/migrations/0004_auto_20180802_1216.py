# Generated by Django 2.0.6 on 2018-08-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20180726_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='img/logo.png', null=True, upload_to='productos/producto'),
        ),
    ]
