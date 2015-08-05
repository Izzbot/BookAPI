from django.db import models
from django.utils import timezone

class Book(models.Model):

    # Title
    title = models.CharField(max_length=200)

    # Author(s)
    authors = models.CharField(max_length=1000)

    # Publication Date
    pub_date = models.DateTimeField(default=timezone.now)

    # Publisher
    publisher = models.CharField(max_length=200)

    # Summary
    summary = models.TextField()

    # Price
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Book URL
    book_url = models.URLField()

    # Cover image URL
    cover_url = models.URLField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
