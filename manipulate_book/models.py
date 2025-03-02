from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.TextField()
    author = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name