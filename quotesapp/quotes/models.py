from django.db import models
from authors.models import Author


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote[:50]}..."

