# Generated by Django 2.2.9 on 2020-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180728_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
