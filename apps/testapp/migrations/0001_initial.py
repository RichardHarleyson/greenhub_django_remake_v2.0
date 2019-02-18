# Generated by Django 2.1.4 on 2019-02-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gdrive_vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_vin', models.CharField(max_length=50)),
                ('veh_folder', models.CharField(blank=True, max_length=100)),
                ('status', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]