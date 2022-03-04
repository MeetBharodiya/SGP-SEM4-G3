from pickle import TRUE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup(models.Model):
    Username=models.CharField(max_length=100,primary_key=TRUE)
    Phone_NO=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    flag=models.IntegerField()

    def __str__(self):
         return self.Username

class Profile(models.Model):
    # this we have to write according to our code just one change is in User
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    forgot_password_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=TRUE)