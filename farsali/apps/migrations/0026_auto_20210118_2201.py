# Generated by Django 3.1.3 on 2021-01-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_auto_20210118_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='codigo',
            field=models.CharField(choices=[('None', 'Ninguno'), ('tienda', 'Tienda'), ('nosotros', 'Nosotros'), ('home', 'Home'), ('contacto', 'Contacto'), ('videos', 'Videos'), ('politicas', 'Politicas'), ('videos', 'Videos')], default='None', max_length=45, unique=True, verbose_name='Codigo'),
        ),
    ]
