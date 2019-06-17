from django.db import models
import datetime

class customer(models.Model):
    checkin_date = models.DateField(default=datetime.datetime.now, blank=True, null=True)
    checkin_time = models.TimeField(blank=True, null=True, default=datetime.datetime.now().time())
    bed = models.CharField(max_length=30,blank=True)
    phone = models.BigIntegerField(blank=True)
    address = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=30,blank=True)
    #image = models.ImageField(blank=True)
    present = models.BooleanField(default=False, blank=False)
    checkout_date = models.DateField(blank=True, null=True, default=datetime.datetime.now) #changed to datefield from timefield
    checkout_time = models.TimeField(blank=True, null=True, default=datetime.datetime.now().time())