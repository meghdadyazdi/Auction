from django.shortcuts import render
from items.models import Item

# Create your views here.


def general_search(request):
    items = Item.objects.filter(title__icontains=request.GET['q'])
    return render(request, "index.html", {"items": items})


def user_item_search(request):
    items_user = Item.objects.filter(seller__icontains=request.user.username)
    return render(request, "index.html", {"items": items_user})


def user_bid_or_bought_search(request):
    items_bid_or_bought_user = Item.objects.filter(highest_bid_user__icontains=request.user.username)
    return render(request, "index.html", {"items": items_bid_or_bought_user})
