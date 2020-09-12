"""
Views for creating a listing.
"""

from django.http import HttpRequest, HttpResponse
from django.template import loader

from . import search

def create_listing_view(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("create_listing.html")
    return HttpResponse(template.render(None, request))

def create_listing(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse(status=405)

    album = request.POST.get("album_text")

    # TODO: figure out weirdness with separating artist title and album title in autofill form
    # maybe need to insert a hidden field that'll get sent along so we can keep a hold of the album art

    return HttpResponse(album)