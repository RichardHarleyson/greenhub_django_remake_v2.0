# Generated by Django 2.1.4 on 2019-07-25 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gh_crm', '0004_auto_20190703_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_file', models.FileField(upload_to='clients/%Y/%m_%d/')),
                ('photo_status', models.BooleanField(default=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gh_crm.Crm_Clients')),
            ],
        ),
    ]
