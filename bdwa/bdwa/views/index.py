"""
Defines the index view for the homepage.
"""

from django.http import HttpRequest, HttpResponse
from django.template import loader

from ..models import Listing

def index_view(request: HttpRequest) -> HttpResponse:
    template  = loader.get_template("index2.html")

    listings = Listing.objects.all()
    listings = [x.to_dict() for x in listings]

    context = {
        "listings": listings
    }

    return HttpResponse(template.render(context, request))