# Generated by Django 3.2.2 on 2021-05-14 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0006_rename_place_indicador_dependencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(choices=[('ESPER', 'Espera de aprobacion'), ('APRO', 'Aprobado'), ('RECHA', 'Rechazado')], max_length=6)),
                ('Observaciones', models.TextField(max_length=100)),
                ('Fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='pedido_papeleria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ti_pape', models.CharField(max_length=30, verbose_name='tipo de papeleria')),
                ('can_pape', models.IntegerField(verbose_name='cantidas papeleria')),
                ('Area_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.tipo_indicador')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.estado')),
            ],
        ),
    ]
