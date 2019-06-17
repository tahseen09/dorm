# Generated by Django 2.2.2 on 2019-06-17 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190602_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkin_time',
            field=models.TimeField(blank=True, default=datetime.time(10, 4, 22, 647754), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 17, 10, 4, 22, 647849), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_time',
            field=models.TimeField(blank=True, default=datetime.time(10, 4, 22, 647859), null=True),
        ),
    ]
