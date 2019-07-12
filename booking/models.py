from django.db import models
import datetime

class customer(models.Model):
    checkin_date = models.DateField(blank=False, null=True)
    checkin_time = models.TimeField(blank=True, null=True)
    bed = models.CharField(max_length=30,blank=True)
    phone = models.BigIntegerField(blank=True)
    address = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True)
    manager = models.CharField(max_length=30,blank=True)
    present = models.BooleanField(default=False, blank=False)
    checkout_date = models.DateField(blank=True, null=True)
    checkout_time = models.TimeField(blank=True, null=True)