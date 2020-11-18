from django.shortcuts import render
from items.models import Item
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator

# Create your views here.


def general_search(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(title__icontains=request.GET['q']).order_by('-published_date')
    check_for_pageing = True
    return render(request, "index.html", {"items": items, 'check_for_pageing': check_for_pageing, 'search': request.GET['q']})


def user_item_search(request):
    items_user = Item.objects.filter(seller__icontains=request.user.username).order_by('-published_date')
    paginator = Paginator(items_user, 5)
    page = request.GET.get('page', 1)
    items_user = paginator.page(page)
    return render(request, "index.html", {"items": items_user})


def user_bid_or_bought_search(request):
    items_bid_or_bought_user = Item.objects.filter(highest_bid_user__icontains=request.user.username).order_by('-published_date')
    paginator = Paginator(items_bid_or_bought_user, 5)
    page = request.GET.get('page', 1)
    items_bid_or_bought_user = paginator.page(page)
    return render(request, "index.html", {"items": items_bid_or_bought_user})


def sort_sold(request):
    items = Item.objects.filter(sold=1).order_by('-published_date')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'sold'})


def sort_new(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    # items = Item.objects.filter(sold=0).order_by('-published_date')
    items = Item.objects.filter(sold=0, published_date__lte=timezone.now()
                                ).order_by('-published_date')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'new'})


def sort_price(request):
    # items = Item.objects.annotate(search=SearchVector('title', 'description', 'price', 'tag', 'published_date'),).filter(search=request.GET['q'])
    items = Item.objects.filter(sold=0, published_date__lte=timezone.now()
                                ).order_by('price')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {"items": items, "mode": 'price'})
