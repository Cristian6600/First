# Generated by Django 3.2.2 on 2021-09-22 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0001_initial'),
        ('users', '0001_initial'),
        ('dotacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.areas')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M_solicitud.sucursal')),
            ],
        ),
    ]
