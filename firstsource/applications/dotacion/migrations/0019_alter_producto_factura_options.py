# Generated by Django 3.2.2 on 2022-09-15 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0018_factura_total_factura'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto_factura',
            options={'verbose_name': 'detalle'},
        ),
    ]
