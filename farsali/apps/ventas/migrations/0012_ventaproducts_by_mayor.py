# Generated by Django 3.1.4 on 2021-01-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_auto_20210122_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventaproducts',
            name='by_mayor',
            field=models.BooleanField(default=False, verbose_name='Cantidad x Mayor'),
        ),
    ]