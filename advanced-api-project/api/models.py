from django.db import models

# Create your models here.

# Define Author and Book models with a ForeignKey relationship
# Define the Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)