# Generated by Django 3.2.2 on 2021-06-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0017_alter_rep_conta_va_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep_conta',
            name='Va_total',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
    ]