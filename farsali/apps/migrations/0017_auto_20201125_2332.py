# Generated by Django 2.2.13 on 2020-11-25 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_auto_20201125_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='background',
            options={'ordering': ('orden',), 'verbose_name': 'Background', 'verbose_name_plural': 'Imágenes Principales'},
        ),
    ]
