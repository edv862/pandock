# Generated by Django 2.2.9 on 2020-04-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_auto_20180815_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]