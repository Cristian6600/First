# Generated by Django 3.2.2 on 2022-09-29 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0002_m_solicitud_n_factura'),
        ('dotacion', '0041_dotacion_ceco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dotacion',
            name='ceco',
        ),
        migrations.AddField(
            model_name='entrega',
            name='ceco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.cecos', verbose_name='Centro de costos'),
            preserve_default=False,
        ),
    ]
