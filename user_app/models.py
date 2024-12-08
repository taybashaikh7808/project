from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    contact= models.TextField()
    #role = models.CharField(max_length=50)