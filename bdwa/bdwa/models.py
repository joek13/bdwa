"""
Database models.
"""

from django.db import models
import random

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
    def __str__(self):
        return self.title

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

    date_created = models.DateTimeField(auto_now_add=True,null = True)
    """
    The date this listing was created.
    """

    def get_absolute_url(self):
        import django.urls
        return django.urls.reverse("show_listing", args=[self.id])
    
    def to_dict(self):
        return {
            "album": self.album.to_dict(),
            "description": self.description,
            "score": self.score,
            "url": self.get_absolute_url()
        }
    def __str__(self):
        return self.description



def get_random_listing(for_album):
    items = Listing.objects.get(album=for_album)
    # if you want only a single random item
    random_item = random.choice(items)

def get_random_album():
    items = Album.objects.all()
    # if you want only a single random item
    return random.choice(items)

def get_albums(n):
    items = Album.objects.all()
    # change 3 to how many random items you want
    random_items = random.sample(items, n)

def sample_listings(n):
    albums = get_albums(n)
    ret = []
    for a in albums:
        ret.append(get_random_listing(a))
    return ret

    
