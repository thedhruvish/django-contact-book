from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)


class Contact(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    c_number = models.IntegerField(unique=True)
    address = models.TextField(max_length=200)
