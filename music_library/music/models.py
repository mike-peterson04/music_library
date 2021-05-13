from django.db import models

class Song(models.Model):
    title = models.Charfield(max_length=50)
    artist = models.Charfield(max_length=50)
    album = models.Charfield(max_length=50)
    release_date = models.DateTimeField()
    likes = models.IntegerField(default=None)