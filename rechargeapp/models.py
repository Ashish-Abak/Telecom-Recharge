from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    email=models.CharField(max_length=100)
    mobile=models.BigIntegerField()

class plan(models.Model):
    DATA=(('1GB','1GB/Day'),('1.5GB','1.5GB/Day'),('2GB','2GB/Day'),('2.5GB','2.5GB/Day'),('3GB','3GB/Day'),('-','-'))
    price=models.IntegerField()
    validity=models.CharField(max_length=50)
    data=models.CharField(max_length=50,choices=DATA)
    is_active=models.BooleanField(default=True)
    total_data=models.CharField(max_length=50)
    voice=models.CharField(max_length=50)
    OTT=models.CharField(max_length=50)
    SMS=models.CharField(max_length=50)
    add_on=models.CharField(max_length=100)
    family=models.CharField(max_length=100)

class recharge_no(models.Model):
    rmobile=models.BigIntegerField()
  
