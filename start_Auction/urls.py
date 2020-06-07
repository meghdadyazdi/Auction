from django.conf.urls import url
from .views import start_auction

urlpatterns = [
    url(r'^(?P<pk>\d+)', start_auction, name='start_auction'),
]
