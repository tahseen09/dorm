# Generated by Django 2.1.8 on 2019-07-09 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20190709_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkin_time',
            field=models.TimeField(blank=True, default=datetime.time(17, 33, 36, 919336), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_time',
            field=models.TimeField(blank=True, default=datetime.time(17, 33, 36, 919473), null=True),
        ),
    ]
