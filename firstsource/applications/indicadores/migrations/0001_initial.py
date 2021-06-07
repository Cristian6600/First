# Generated by Django 3.2.2 on 2021-06-07 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_indicador',
            fields=[
                ('Tipo', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tipo de indicador',
                'verbose_name_plural': 'Tipo de indicadores',
            },
        ),
        migrations.CreateModel(
            name='indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Nomviembre', 'Nomviembre'), ('Diciembre', 'Diciembre')], max_length=10)),
                ('Año', models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', ''), ('2024', ''), ('2025', '')], max_length=4)),
                ('meta', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Gestionad@s')),
                ('limite', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Totales')),
                ('aspectos', models.TextField(max_length=100, verbose_name='Aspectos a destacar del mes')),
                ('solicitud', models.TextField(max_length=100, verbose_name='Solicitudes de recursos')),
                ('Porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('Tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.tipo_indicador', verbose_name='indicador')),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadores',
            },
        ),
    ]
