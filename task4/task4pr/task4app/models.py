import self as self
from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
     names=models.CharField(max_length=250)
     imgs=models.ImageField(upload_to='pics')
     descp=models.TextField()





