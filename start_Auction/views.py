from django.shortcuts import render, get_object_or_404
from items.models import Item

# Create your views here.


def start_auction(request, pk):
    """
    start the auction
    """
    item = get_object_or_404(Item, pk=pk)
    if (request.POST.get('end-time-fix-form') and (request.POST.get('auction-time-form'))):
        item.auction_end_time = request.POST.get('end-time-fix-form')
        item.auction_duration_time = request.POST.get('auction-time-form')
        item.highest_bid_offer = item.price
        item.auction_status = 1
        print(item.auction_end_time)
        print(item.auction_duration_time)
    elif (request.POST.get('higher-bid-user') and (request.POST.get('higher-bid'))):
        bid = int(request.POST.get('higher-bid'))
        item.highest_bid_offer = item.highest_bid_offer + bid
        item.highest_bid_user = request.POST.get('higher-bid-user')
        print(item.auction_end_time)
        print(item.auction_duration_time)
    item.save()
    return render(request, "itemdetail.html", {'item': item})
