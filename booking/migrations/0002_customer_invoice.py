# Generated by Django 2.2.3 on 2019-07-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='invoice',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
