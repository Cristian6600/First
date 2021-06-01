# Generated by Django 3.2.2 on 2021-06-01 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clasificaciones', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(blank=True, choices=[('ESPER', 'Espera de aprobacion'), ('APRO', 'Aprobado'), ('RECHA', 'Rechazado')], max_length=6)),
                ('Observaciones', models.TextField(blank=True, max_length=100)),
                ('Fecha', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proveedores', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sucursal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='pedido_papeleria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ti_pape', models.CharField(max_length=30, verbose_name='tipo de papeleria')),
                ('can_pape', models.IntegerField(verbose_name='cantidad papeleria')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.estado')),
            ],
        ),
        migrations.CreateModel(
            name='m_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_ingreso', models.DateField()),
                ('f_pago', models.DateField()),
                ('f_contabilidad', models.DateField()),
                ('V_gasto', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('V_total', models.IntegerField()),
                ('Clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.clasificacion')),
                ('Sucursal', models.ManyToManyField(to='M_solicitud.Sucursal')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.proveedor')),
            ],
        ),
    ]
