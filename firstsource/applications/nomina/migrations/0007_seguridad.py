# Generated by Django 3.2.2 on 2021-06-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0006_alter_cargue_total_descuentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.CharField(max_length=10)),
                ('Identificacion', models.CharField(max_length=15)),
                ('Provision', models.CharField(max_length=20)),
                ('Cta', models.IntegerField()),
                ('D_C', models.CharField(max_length=1)),
                ('Valor', models.DecimalField(decimal_places=3, max_digits=12)),
                ('Nombre', models.CharField(max_length=60)),
                ('Centro_Costo', models.CharField(max_length=20)),
                ('Concepto', models.CharField(max_length=15)),
            ],
        ),
    ]
