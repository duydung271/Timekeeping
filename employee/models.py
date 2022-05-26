from email.policy import default
from django.db import models

# Create your models here.
GENDER_CHOICES = ((0,"Unkown"),(1,"Female"),(2,"Male"))

class Employee(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    birthDay = models.DateField(default='2000-01-01')
    homeTown = models.CharField(max_length=100, default="Unkown")
    phone = models.CharField(max_length=20, default="Unkown")
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    educationLevel = models.CharField(max_length=100, default="Unkown")

    avatar = models.ImageField(default = 'unkown.jpg')
    embedding = models.BinaryField()

    def __str__(self):
        return f'{self.id} - {self.name}'
