# Generated by Django 2.0.6 on 2018-08-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0009_receta_slider_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='titulo_resumido',
            field=models.CharField(default='', max_length=200, verbose_name='Titulo para el tab de receta'),
            preserve_default=False,
        ),
    ]
