# Generated by Django 3.2.2 on 2022-12-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0003_alter_detalle_vehiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='factura_vehiculo',
            field=models.IntegerField(default=1, verbose_name='FACTURA POR VEHICULO'),
            preserve_default=False,
        ),
    ]