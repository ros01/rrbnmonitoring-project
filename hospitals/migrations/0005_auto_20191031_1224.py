# Generated by Django 2.1.7 on 2019-10-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0004_auto_20191031_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.AutoField(default=100000, primary_key=True, serialize=False, unique=True),
        ),
    ]
