# Generated by Django 2.2.3 on 2019-07-14 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190714_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='duration',
        ),
    ]
