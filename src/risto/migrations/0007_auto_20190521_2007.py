# Generated by Django 2.2.1 on 2019-05-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risto', '0006_auto_20190520_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]