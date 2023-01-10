
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from zaid.mainapp.views import auctions
urlpatterns = [
    path("auctions/", auctions.auctions, name="auctions"),
    path("auctions/<int:auction_id>",auctions.show_auction,name='show_auction'),
    path("auctions/new/", auctions.new_auction, name="new_auction"),
    path("auctions/create/", auctions.create_auction, name="create_auction"),

]