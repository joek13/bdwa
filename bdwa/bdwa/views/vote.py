"""
Views for voting on a listing.
"""

import uuid, base64
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.db.models import F

from ..models import Listing

def _generate_id():
    uuid = uuid.uuid4()
    return base64.encode(uuid.bytes) # base64 encoded uuid

def generate_id_cookie(request: HttpRequest) -> HttpResponse:
    id_cookie = request.COOKIES.get("uid")
    response = HttpResponse()
    if id_cookie is None:
        response.set_cookie("uid", _generate_id())

def vote_listing(request: HttpRequest, listing_id: int, sign: int) -> JsonResponse:
    if request.method != "POST":
        return HttpResponse(status=405)

    listing = Listing.objects.get(id__exact=listing_id)

    # hack: odd numbers increment, even numbers decrement
    if sign % 2 == 1:
        sign = 1
    else:
        sign = -1

    listing.score = F("score") + sign
    listing.save(update_fields=["score"])

    return JsonResponse ({
        "new_score": Listing.objects.get(id__exact=listing_id).score
    })