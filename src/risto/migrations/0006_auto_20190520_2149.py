# Generated by Django 2.2.1 on 2019-05-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risto', '0005_auto_20190520_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
