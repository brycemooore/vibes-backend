from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    spotify_id = models.CharField(max_length=50)

    class Meta:
        ordering = (['title'])

        def __str__(self):
            return self.title + ' by ' + self.artist

class User(models.Model):
    username = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    songs = models.ManyToManyField(Song)

    class Meta:
        ordering = (['username'])

        def __str__(self):
            return self.username




