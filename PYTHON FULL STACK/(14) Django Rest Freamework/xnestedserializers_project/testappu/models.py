from django.db import models

# Create your models here.
class Author(models.Model):             # this model(table) is primary table
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)

    # if enywhere author object is going to display then internally __str__ method is going to call
    def __str__(self):
        return self.first_name
    
class Book(models.Model):             # this model(table) is secondary table as it have foreign key refrence to author table means it depends on author table
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_by_author')  # 1st param = which table it is associated with ... 2nd param = if you delete any author in table then corresponding book also get deleted .... 3rd param = related name if we use on the author object then books information we are going to get
    release_date = models.DateField()
    rating = models.IntegerField() 

    # if any person tryping to print book then it will print title of book
    def __str__(self):
        return self.title