from django.conf.urls import url
from .views import payment

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', payment, name='payment'),
]
