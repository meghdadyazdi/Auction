"""auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from items import urls as urls_items
from start_Auction import urls as urls_start_Auction
from django.views.static import serve
# from item.views import get_items
from .settings import MEDIA_ROOT
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='items/')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^items/', include(urls_items)),
    url(r'^items/', include(urls_start_Auction)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
