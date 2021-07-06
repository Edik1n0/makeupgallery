# Generated by Django 3.1.3 on 2021-01-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0025_auto_20210118_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion_adicional',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Descripcion Adicional del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_no_prefer',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Descripcion del producto no prefer'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_prefer',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Descripcion del producto prefer'),
        ),
    ]