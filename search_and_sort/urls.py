from django.conf.urls import url
from .views import general_search, user_bid_or_bought_search, user_item_search, sort_sold, sort_new, sort_price
urlpatterns = [
    url(r'^$', general_search, name='search'),
    url(r'^user-items/$', user_item_search, name='search_user'),
    url(r'^user-bid/$', user_bid_or_bought_search, name='search_bid_or_bought_user'),
]