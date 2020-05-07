from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name
