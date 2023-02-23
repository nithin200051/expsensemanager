from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    name = models.CharField(max_length=255,default=None)
    email = models.EmailField(unique=True,default=None)
    phone = models.CharField(max_length=20,default=None)
    password = models.CharField(max_length=255,default=None)

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category_id = models.IntegerField(default=None)
    date = models.DateField(auto_now_add=None)

    def __str__(self):
        return self.amount


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category_id = models.IntegerField(default=None)
    date = models.DateField(auto_now_add=None)

    def __str__(self):
        return self.amount


class Category(models.Model):
    category_id=models.IntegerField(default=None)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
     
