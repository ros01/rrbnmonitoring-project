# Generated by Django 2.1.7 on 2019-11-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='module_name',
            field=models.CharField(choices=[('Monitoring HQ', 'MonitoringHq'), ('Enugu Zonal Office', 'EnuguOffice'), ('Registrars Office', 'CEO'), ('Accounts HQ', 'FAH')], max_length=20),
        ),
    ]