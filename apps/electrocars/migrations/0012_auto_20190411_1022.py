# Generated by Django 2.1.4 on 2019-04-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0011_auto_20190411_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='veh_type',
            field=models.CharField(choices=[('salon', 'salon'), ('dealler', 'dealler')], default=('salon', 'salon'), max_length=20),
        ),
    ]
