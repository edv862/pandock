# Generated by Django 2.0.6 on 2018-07-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_noticia_posicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/noticias'),
        ),
    ]
