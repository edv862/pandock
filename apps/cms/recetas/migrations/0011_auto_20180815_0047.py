# Generated by Django 2.0.6 on 2018-08-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0010_receta_titulo_resumido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='titulo_resumido',
            field=models.CharField(max_length=18, verbose_name='Titulo para el tab de receta'),
        ),
    ]