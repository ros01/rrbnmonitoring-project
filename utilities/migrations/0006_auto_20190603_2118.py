# Generated by Django 2.1.7 on 2019-06-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0005_auto_20190603_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('E', 'Expired')], max_length=1),
        ),
    ]
