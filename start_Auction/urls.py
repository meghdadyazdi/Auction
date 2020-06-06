from django.conf.urls import url
from .views import start_auction, restart_auction

urlpatterns = [
    url(r'^(?P<pk>\d+)', start_auction, name='start_auction'),
    url(r'^(?P<pk>\d+)', restart_auction, name='restart_auction')
]
