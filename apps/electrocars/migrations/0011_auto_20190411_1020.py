# Generated by Django 2.1.4 on 2019-04-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0010_auto_20190226_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='veh_type',
            field=models.CharField(choices=[('salon', 'dealler')], default=('salon', 'dealler'), max_length=20),
        ),
    ]
