# Generated by Django 2.2.2 on 2019-06-17 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20190617_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkin_time',
            field=models.TimeField(blank=True, default=datetime.time(10, 9, 37, 290509), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_time',
            field=models.TimeField(blank=True, default=datetime.time(10, 9, 37, 290585), null=True),
        ),
    ]
