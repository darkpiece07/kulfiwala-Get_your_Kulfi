from django.db import models
from phone_field import PhoneField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = PhoneField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    name = models.CharField(max_length=50, default="username", )
    email = models.CharField(max_length=50, default="username@gmail.com")
    phone = PhoneField(default="+91-9999999999")
    job_profile = models.CharField(max_length=50, default="Job profile")
    avatar = models.ImageField(upload_to='profile_pics/', default="static/avatar.png")
    
    url1 = models.URLField(max_length=50, default="url")
    address = models.CharField(max_length=200, default="address")

    def __str__(self):
        return self.name
    

class Kulfi(models.Model):
    kulfi_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    kulfi_pic = models.ImageField()
    ingredients = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.kulfi_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    