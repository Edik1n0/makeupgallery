# Generated by Django 2.2.13 on 2020-11-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Direccion'),
        ),
    ]