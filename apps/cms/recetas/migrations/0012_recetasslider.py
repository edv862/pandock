# Generated by Django 2.0.6 on 2018-08-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0011_auto_20180815_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecetasSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='receta_slider')),
            ],
        ),
    ]
