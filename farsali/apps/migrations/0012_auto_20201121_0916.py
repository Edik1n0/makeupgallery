# Generated by Django 2.2.13 on 2020-11-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_background_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Video'),
        ),
    ]