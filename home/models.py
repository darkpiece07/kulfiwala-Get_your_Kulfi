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
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = PhoneField()
    job_profile = models.CharField(max_length=50)
    
    url1 = models.URLField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name