from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    year=models.IntegerField()
    course=models.CharField(max_length=200)