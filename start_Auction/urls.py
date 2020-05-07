from django.conf.urls import url
from .views import start_auction, start_bid

urlpatterns = [
    url(r'^(?P<pk>\d+)', start_auction, name='start_auction'),
    url(r'^(?P<pk>\d+)', start_bid, name='start_bid'),
]
