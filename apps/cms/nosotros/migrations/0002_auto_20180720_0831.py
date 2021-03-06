# Generated by Django 2.0.6 on 2018-07-20 08:31

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nosotros',
            options={'verbose_name': 'Nosotros', 'verbose_name_plural': 'Nosotros'},
        ),
        migrations.AddField(
            model_name='nosotros',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='nosotros',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
