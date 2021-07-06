# Generated by Django 2.2.13 on 2020-11-18 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.PositiveIntegerField(default=0, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.CharField(default='', max_length=100, verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='locacion',
            field=models.CharField(default='', max_length=100, verbose_name='Locación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nick_name',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Nick Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='is_farsali',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Es cliente Farsali'),
        ),
    ]
