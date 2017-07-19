from __future__ import unicode_literals

from django.db import models

# a Class in a model automatically creates a DB table with sqlite (per settings.py file).
# vars would create columns

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
