from django.db import models

# Create your models here.
# models = module(i.e. file)    
# model is a class inside module models
class Details(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    marks=models.IntegerField()

class Employee(models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    department=models.CharField(max_length=100,null=True)
"""
orm --> oject relational mapper
        ORM enables us interact with databases in more pathonic way like we can avoid writing row queries 
        it is possible to access save delete and perform other operations over the datbase without ever writing sql queries
        it works as abstraction layer between the models and database 
mysql is used to interact with database 
mysql has queries which are get fired

"""
