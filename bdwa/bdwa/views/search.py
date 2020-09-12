"""
Album search endpoint.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import re

def search_albums(request: HttpRequest, limit = 10) -> JsonResponse:
    query = request.GET.get("q")

    if query is None:
        raise ValueError("query cannot be None.")

    # TODO: cache-control?
    results = _search(query)[0:limit]
    return JsonResponse({"results": results})

def _search(query):
    resp = requests.get(f"https://www.last.fm/search/albums?q={query}")
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, features="html.parser")

    return [
        {
            "url":
            re.sub("(\d+s)", "300x300",
                   x.find("img").attrs["src"]
                ),
            "album":
            x.find("h4").a.text,
            "artist":
            x.find("p").a.text,
        } for x in soup.findAll("div", {"class": "album-result-inner"})
    ]