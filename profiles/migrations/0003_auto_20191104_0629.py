# Generated by Django 2.1.7 on 2019-11-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191103_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='module_name',
            field=models.CharField(choices=[('Monitoring HQ', 'MonitoringHq'), ('Enugu Office', 'EnuguOffice'), ('Registrars Office', 'CEO'), ('Accounts HQ', 'FAH')], max_length=20),
        ),
    ]
