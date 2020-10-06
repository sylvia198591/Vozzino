from django.db import models
# from PIL import Image
# Create your models here.

class Employee(models.Model):
    Name=models.CharField(max_length=200)
    Telephone=models.IntegerField()
    Age=models.IntegerField()
    Profile_pic=models.ImageField(upload_to='images')
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    isActive=models.BooleanField(default=False)
    isLog = models.BooleanField(default=False)
    def __str__(self):
        return self.Username
