# Generated by Django 2.1.4 on 2019-04-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0012_auto_20190411_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='veh_type',
            field=models.CharField(choices=[('salon', 'салон'), ('dealler', 'диллер')], default=('salon', 'салон'), max_length=20),
        ),
    ]
