# Generated by Django 2.1.4 on 2019-02-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0006_auto_20190213_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_photos',
            name='type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
