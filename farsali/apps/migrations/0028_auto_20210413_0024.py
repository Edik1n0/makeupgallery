# Generated by Django 3.1.3 on 2021-04-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0027_auto_20210412_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constante',
            name='nombre',
            field=models.CharField(choices=[('None', 'Ninguno'), ('contacto_email', 'Email'), ('contacto_telefono1', 'Teléfono'), ('contacto_telefono2', 'Télefono 2'), ('contacto_direccion', 'Dirección'), ('email_notificacion', 'Email Notificacion'), ('monto_max', 'Monto Máximo de Compra')], default='None', max_length=45, unique=True, verbose_name='Codigo'),
        ),
    ]
