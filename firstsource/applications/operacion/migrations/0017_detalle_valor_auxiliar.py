# Generated by Django 3.2.2 on 2022-12-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0016_alter_detalle_efectividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='valor_auxiliar',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]