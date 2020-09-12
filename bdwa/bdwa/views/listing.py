"""
Views for creating a listing.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django import urls

import json

from . import search
from ..models import Album, Listing

def create_listing_view(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("create_listing.html")
    return HttpResponse(template.render(None, request))

def show_listing_view(request: HttpResponse, listing_id: int) -> HttpResponse:
    """
    View for displaying a single listing.
    """
    template = loader.get_template("show_listing.html")

    listing = Listing.objects.get(id__exact = listing_id)

    return HttpResponse(template.render(listing.to_dict(), request))

def create_listing(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse(status=405) # post only

    album_json = request.POST.get("album") # load album info string
    if album_json is None:
        raise ValueError("album parameter cannot be None")
    album_info = json.loads(album_json)

    description = request.POST.get("description")
    if description is None:
        raise ValueError("description cannot be None")

    description = description.strip().replace("\n", " ")

    # get or create album
    album, created = Album.objects.get_or_create(
        title = album_info["album"],
        artist = album_info["artist"],
        album_art = album_info["url"]
    )

    # create listing with this album
    listing = Listing.objects.create(
        album = album,
        description = description,
        score = 0
    )

    listing.save()
    
    # redirect to "view listing" page
    return redirect(listing.get_absolute_url()) # redirect to show_listing page