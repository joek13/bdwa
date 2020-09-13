"""
Defines the index view for the homepage.
"""

from django.http import HttpRequest, HttpResponse
from django.template import loader

from ..models import Listing, get_albums, get_random_listing
import random

SPLASHES = [
    "Discover new music with mysterious crowdsourced descriptions.",
    "Put someone on to your favorite album.",
    "Less trauma than Tinder, or your money back.",
    "Find your musical match.",
    "Find your next big phase.",
]

def index_view(request: HttpRequest) -> HttpResponse:
    template  = loader.get_template("index2.html")

    albums = get_albums(9)
    listings = [get_random_listing(album) for album in albums]
    listings = [x.to_dict() for x in listings]

    context = {
        "listings": listings,
        "splash": random.choice(SPLASHES)
    }

    return HttpResponse(template.render(context, request))

def about_view(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("about.html")

    return HttpResponse(template.render(None, request))