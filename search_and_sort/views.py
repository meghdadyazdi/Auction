from django.shortcuts import render
from items.models import Item
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator

# Create your views here.


def general_search(request):
    """
    Return a list of items that are searched by a keyword.
    """
    items = Item.objects.filter(title__icontains=request.GET['q']).order_by('-published_date')
    check_for_pageing = True
    return render(request, "index.html", {"items": items, 'check_for_pageing': check_for_pageing, 'search': request.GET['q']})


def user_item_search(request):
    """
    Return a list of items selling by active user.
    """
    items_user = Item.objects.filter(seller__icontains=request.user.username).order_by('-published_date')
    paginator = Paginator(items_user, 5)
    page = request.GET.get('page', 1)
    items_user = paginator.page(page)
    return render(request, "index.html", {"items": items_user})


def user_bid_or_bought_search(request):
    """
    Return a list of items bidded by active user.
    """
    items_bid_or_bought_user = Item.objects.filter(highest_bid_user__icontains=request.user.username).order_by('-published_date')
    paginator = Paginator(items_bid_or_bought_user, 5)
    page = request.GET.get('page', 1)
    items_bid_or_bought_user = paginator.page(page)
    return render(request, "index.html", {"items": items_bid_or_bought_user})


def sort_sold(request):
    """
    Return a list of sold items.
    """
    items = Item.objects.filter(sold=1).order_by('-published_date')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'sold'})


def sort_new(request):
    """
    Return a list of new items.
    """
    items = Item.objects.filter(sold=0, published_date__lte=timezone.now()
                                ).order_by('-published_date')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'new'})


def sort_price(request):
    """
    Return a list of items sorted by price.
    """
    items = Item.objects.filter(sold=0, published_date__lte=timezone.now()
                                ).order_by('price')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'price'})
