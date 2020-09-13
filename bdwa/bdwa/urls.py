"""bdwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.index_view, name="index"),
    path("albums/", views.search.search_albums, name="albums"),
    path('search/', views.search.search_listings, name="search_listings"),
    path("create/", views.listing.create_listing_view, name="create_listing"),
    path("listing/<int:listing_id>", views.listing.show_listing_view, name="show_listing"),
    path('admin/', admin.site.urls),
    path("api/create_listing/", views.listing.create_listing, name="create_listing_api"),
    path("api/vote_listing/<int:listing_id>/<int:sign>", views.vote.vote_listing, name="vote_listing_api"),
]
