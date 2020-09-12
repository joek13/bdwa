"""
Database models.
"""

from django.db import models

class Genre(models.Model):
    """
    A genre
    """
    name = models.TextField()

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

    album_art = models.URLField()
    """
    Link to album art.
    """
    
    genre = models.ManyToManyField(Genre)
    """
    The album's genre.
    """

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album_art": self.album_art
        }

class Listing(models.Model):
    """
    A user-contributed listing of a given album.
    """

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    """
    The album this listing describes.
    """

    description = models.CharField(max_length=280)
    """
    User-contributed description of this Album.
    """  
    score = models.IntegerField()
    """
    Crowd-determined score of the listing
    """

    def get_absolute_url(self):
        import django.urls
        return django.urls.reverse("show_listing", args=[self.id])
    
    def to_dict(self):
        return {
            "album": self.album.to_dict(),
            "description": self.description,
            "score": self.score
        }

