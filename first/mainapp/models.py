from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Product(models.Model):
    apple = models.CharField(max_length=30)
    cucumber = models.CharField(max_length=30)

class ProductCategory(models.Model):
    vegetables = models.CharField(max_length=30)
    fruits = models.CharField(max_length=30)