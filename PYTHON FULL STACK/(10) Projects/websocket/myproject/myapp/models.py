from django.db import models

# Create your models here.
class Student(models.Model):
    client_name=models.CharField(max_length=200)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=200)
    assigned_user=models.CharField(max_length=200)
    status=models.CharField(max_length=200)