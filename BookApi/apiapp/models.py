from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField()
    
class Customer_Order(models.Model):
    login_name = models.ForeignKey(User,models.DO_NOTHING)
    booksborrowed = models.ForeignKey(Book,models.DO_NOTHING)
    
