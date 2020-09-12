"""
Database models.
"""

from django.db import models

class Album(models.Model):
    """
    A single album, which might have multiple listings.
    """

    title = models.TextField()
    """
    The album title.
    """

    artist = models.TextField()
    """
    The album's artist.
    """

class Listing(models.Model):
    """
    A user-contributed listing of a given album.
    """

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    """
    The album this listing describes.
    """

    description = models.TextField()
    """
    User-contributed description of this Album.
    """