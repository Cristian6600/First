# Generated by Django 3.2.2 on 2022-09-14 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0011_author_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cantidad',
        ),
        migrations.CreateModel(
            name='Producto_factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('dotacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotacion.dotacion')),
            ],
        ),
    ]
