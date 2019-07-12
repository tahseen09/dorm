# Generated by Django 2.1.4 on 2019-07-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190712_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkin_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='checkout_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
