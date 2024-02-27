from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    grade=models.CharField(max_length=10)
    