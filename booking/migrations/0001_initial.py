# Generated by Django 2.1.4 on 2019-05-29 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('time', models.TimeField(blank=True, default=datetime.time(20, 32, 18, 307145))),
                ('bed', models.CharField(blank=True, max_length=30)),
                ('phone', models.BigIntegerField(blank=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
    ]
