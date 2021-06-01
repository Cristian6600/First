# Generated by Django 3.2.2 on 2021-06-01 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Articulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hardware', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='inmobiliario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20)),
                ('Descripcion', models.CharField(max_length=20)),
                ('Piso', models.IntegerField()),
                ('Observacion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=45)),
                ('software', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=30)),
                ('Modelo', models.CharField(max_length=30)),
                ('Estado', models.BooleanField(default=False)),
                ('Observacion', models.TextField(max_length=250)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('Mac', models.CharField(max_length=20)),
                ('Ram', models.CharField(blank=True, max_length=6)),
                ('Disco', models.CharField(blank=True, max_length=30)),
                ('Procesador', models.CharField(blank=True, max_length=15)),
                ('Usb', models.BooleanField(blank=True, default=False)),
                ('Hdmi', models.BooleanField(blank=True, default=False)),
                ('Vga', models.BooleanField(blank=True, default=False)),
                ('Bloq_ex', models.BooleanField(blank=True, default=False, verbose_name='Bloqueo de extraibles')),
                ('bloq_pa', models.BooleanField(blank=True, default=False, verbose_name='Bloqueo de panel de control')),
                ('Licencia', models.ManyToManyField(to='inventario.Licencia')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marcas')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.hardware', verbose_name='Hardware')),
            ],
        ),
    ]
