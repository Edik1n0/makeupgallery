# Generated by Django 3.1.3 on 2021-02-22 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0026_auto_20210128_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaproducto',
            options={'ordering': ('orden', 'id'), 'verbose_name': 'Categoría Producto', 'verbose_name_plural': 'Categorías Productos'},
        ),
        migrations.AddField(
            model_name='galeriaproducto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
