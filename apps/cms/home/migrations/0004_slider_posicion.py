# Generated by Django 2.0.6 on 2018-07-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180720_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='posicion',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1'),
        ),
    ]
