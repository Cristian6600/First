# Generated by Django 3.2.2 on 2021-05-14 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='dependencia',
        ),
    ]
