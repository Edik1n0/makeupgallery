# Generated by Django 2.2.13 on 2020-11-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20201116_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='referencia',
            field=models.CharField(max_length=150, unique=True, verbose_name='Referencia'),
        ),
    ]
