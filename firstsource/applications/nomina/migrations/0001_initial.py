# Generated by Django 3.2.2 on 2021-06-01 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Identificacion', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=40)),
                ('CODIGO_CC', models.CharField(max_length=10)),
                ('Cuenta_Contable', models.IntegerField()),
                ('Tipo', models.CharField(max_length=3)),
                ('Valor', models.IntegerField()),
                ('Nombre', models.CharField(max_length=80)),
                ('Concepto', models.CharField(max_length=50)),
            ],
        ),
    ]
