# Generated by Django 2.1.7 on 2019-10-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]
