# Generated by Django 3.1.3 on 2020-12-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0019_auto_20201217_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion_no_prefer',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion del producto no prefer'),
        ),
    ]