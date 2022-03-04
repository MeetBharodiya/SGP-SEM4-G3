from pickle import TRUE
from django.db import models

# Create your models here.
class chef(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Username=models.CharField(max_length=20,primary_key=TRUE)
    Phone_NO=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=50)