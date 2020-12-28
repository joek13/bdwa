"""
Album search endpoint.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader

from ..models import Listing, Album

import requests
from bs4 import BeautifulSoup
import re

from django.db.models import Q


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search_listings(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query is None or query == "":
        template = loader.get_template("search.html")
        return HttpResponse(template.render(None, request))

    # search for listings whose description match the string
    # or maybe listings whose albums also match??
    entry_query = get_query(
        query, ['description', "album__title", "album__artist"])

    results = Listing.objects.filter(entry_query, approved=True)
    # results = Listing.objects.annotate(
    #  search=SearchVector('description'),
    #   ).filter(search=query)

    # results = Listing.objects.filter(description__search=query)

    template = loader.get_template("search_results.html")

    context = {
        "results": [x.to_dict() for x in results],
        "query": query
    }

    return HttpResponse(template.render(context, request))


def search_albums(request: HttpRequest, limit=10) -> JsonResponse:
    query = request.GET.get("q")

    if query is None:
        raise ValueError("'q' parameter cannot be None.")

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
