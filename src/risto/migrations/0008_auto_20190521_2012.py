# Generated by Django 2.2.1 on 2019-05-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risto', '0007_auto_20190521_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
