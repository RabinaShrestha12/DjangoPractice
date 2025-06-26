from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)


