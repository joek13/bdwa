"""
Defines the index view for the homepage.
"""

from django.http import HttpRequest, HttpResponse
from django.template import loader

def index_view(request: HttpRequest) -> HttpResponse:
    template  = loader.get_template("index.html")

    context = None

    return HttpResponse(template.render(context, request))