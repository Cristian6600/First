# Generated by Django 3.2.2 on 2021-06-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0003_auto_20210613_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_solicitud',
            name='V_gasto',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
        migrations.AlterField(
            model_name='m_solicitud',
            name='iva',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]