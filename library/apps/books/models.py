from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=100, blank=True)
    edition = models.CharField(max_length=100, blank=True)
    publication_year = models.DateTimeField(auto_now=timezone.now)
    authors = models.ManyToManyField(
        'authors.Author',
        related_name='authors'
    )

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name} - Edition: {self.edition}'
