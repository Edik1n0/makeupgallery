# Generated by Django 3.1.3 on 2021-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0029_descuentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentos',
            name='categorias_productos',
            field=models.ManyToManyField(blank=True, null=True, related_name='descuento_productos', to='inventario.CategoriaProducto', verbose_name='CategoriaProducto'),
        ),
        migrations.AlterField(
            model_name='descuentos',
            name='productos',
            field=models.ManyToManyField(blank=True, null=True, related_name='descuento_productos', to='inventario.Producto', verbose_name='Producto'),
        ),
    ]
