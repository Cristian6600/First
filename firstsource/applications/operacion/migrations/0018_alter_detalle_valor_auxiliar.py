# Generated by Django 3.2.2 on 2022-12-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0017_detalle_valor_auxiliar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='valor_auxiliar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
