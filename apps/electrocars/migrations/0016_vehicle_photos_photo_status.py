# Generated by Django 2.1.4 on 2019-07-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrocars', '0015_auto_20190703_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_photos',
            name='photo_status',
            field=models.BooleanField(default=True),
        ),
    ]
