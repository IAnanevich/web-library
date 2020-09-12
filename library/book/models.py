from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

