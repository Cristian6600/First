# Generated by Django 3.2.2 on 2021-06-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0028_delete_prov_cont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep_costos',
            name='Ceco',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]