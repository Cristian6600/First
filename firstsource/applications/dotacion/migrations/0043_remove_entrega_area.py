# Generated by Django 3.2.2 on 2022-09-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0042_auto_20220929_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='area',
        ),
    ]