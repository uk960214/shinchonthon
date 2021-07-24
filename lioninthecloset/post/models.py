from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
    size_choices = (
        ('XS', 'xs'),
        ('S', 's'),
        ('M', 'm'),
        ('L', 'l'),
        ('XL', 'xl'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    category = models.ForeignKey('Category', on_delete=CASCADE)
    color_main = models.IntegerField(default=0)
    color_sub = models.IntegerField(default=0)
    size = models.CharField(
        max_length=4,
        choices=size_choices,
        default='top',
    )
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag

class Combination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Item = models.ManyToManyField('Item', blank=True)

    def __str__(self):
        return self.name