# Generated by Django 3.2.2 on 2021-06-21 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0018_alter_rep_conta_va_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rep_conta',
            options={'verbose_name': 'Reporte contable', 'verbose_name_plural': 'Reporte contable'},
        ),
        migrations.CreateModel(
            name='rep_Costos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_factura', models.CharField(max_length=30)),
                ('Proveedor', models.CharField(max_length=70)),
                ('Fecha', models.DateField()),
                ('Valor', models.DecimalField(decimal_places=0, max_digits=12)),
                ('Iva', models.DecimalField(decimal_places=0, max_digits=12)),
                ('Va_total', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('Observaciones', models.TextField(max_length=100)),
                ('Ceco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.cecos')),
            ],
            options={
                'verbose_name': 'Reporte Costos',
                'verbose_name_plural': 'Reporte costos',
            },
        ),
    ]