from django.db import models
from datetime import datetime


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    born_date = models.DateTimeField(default=datetime.now)
    born_location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name




