from __future__ import unicode_literals
from django.db import models
class Reg(models.Model):
    user = models.CharField(primary_key=True,max_length=20)
    pwd = models.CharField(max_length=20)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    dob=models.DateField()
    mobno=models.IntegerField()
