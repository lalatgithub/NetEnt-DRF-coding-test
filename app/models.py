from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.conf import settings


@python_2_unicode_compatible
class Book(models.Model):
    """
    We are considering for this model that a Book may have single author, So we are making
    one-to-many relationship with User model

    1) Book belongs to Author.
    2) Author may have multiple Books
    """
    title = models.CharField(max_length=200)
    published_at = models.DateField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    genres = models.ManyToManyField('Genre', related_name='genres')

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
