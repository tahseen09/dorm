# Generated by Django 2.1.4 on 2019-07-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190712_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkin_date',
            field=models.DateField(null=True),
        ),
    ]