# Generated by Django 3.2.2 on 2022-09-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0026_devolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]