from django.conf.urls import url
from .views import get_items, item_detail, add_or_edit_item
from search_and_sort.views import sort_new, sort_price, sort_sold

urlpatterns = [
    url(r'^$', sort_new, name='sort_new'),
    url(r'^price$', sort_price, name='sort_price'),
    url(r'^sold$', sort_sold, name='sort_sold'),
    url(r'^all$', get_items, name='get_items'),
    url(r'^(?P<pk>\d+)/$', item_detail, name='item_detail'),
    url(r'^new/$', add_or_edit_item, name='new_item'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_item, name='edit_item')
]
