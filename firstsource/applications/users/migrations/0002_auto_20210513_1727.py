# Generated by Django 3.2.2 on 2021-05-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='dependencia',
            field=models.ManyToManyField(to='users.dependencia'),
        ),
    ]
