from django.db import models

# Create your models here.

class Customer(models.Model):
    Check_In_Date = models.DateField()
    Check_Out_Date = models.DateField()
    Child_Count = models.IntegerField()
    Adult_Count = models.IntegerField()



