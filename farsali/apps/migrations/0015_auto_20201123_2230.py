# Generated by Django 2.2.13 on 2020-11-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0014_auto_20201123_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constante',
            name='enlace_texto',
            field=models.CharField(blank=True, default='', help_text='En caso de ser una constante que requiera un valor y un enlace externo', max_length=200, null=True, verbose_name='Enlace'),
        ),
    ]