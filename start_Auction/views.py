from django.shortcuts import render, get_object_or_404
from items.models import Item

# Create your views here.


def start_auction(request, pk):
    """
    start the auction
    """
    item = get_object_or_404(Item, pk=pk)
    item.auction_status = 1
    item.auction_end_time = request.POST.get('end-time-fix-form')
    item.auction_duration_time = request.POST.get('auction-time-form')
    item.price = request.POST.get('auction-price-form')
    print(item.auction_end_time)
    print(item.auction_duration_time)
    item.save()
    return render(request, "itemdetail.html", {'item': item})


def start_bid(request, pk):
    """
    bidding
    """
    item = get_object_or_404(Item, pk=pk)
    # item.highest_bid_offer = request.POST.get('higher-bid')
    # item.highest_bid_user = request.POST.get('higher-bid-user')
    # print(item.highest_bid_offer)
    # print(item.highest_bid_user)
    # item.save()
    return render(request, "itemdetail.html", {'item': item})

# def start_bid(request, pk):
#     """
#     bidding
#     """
#     bid_info.objects.filter(pk=pk).highest_bid_offer = request.POST.get('higher-bid')
#     bid_info.objects.filter(pk=pk).highest_bid_user = request.POST.get('higher-bid-user')
#     print(bid_info.objects.filter(pk=pk).highest_bid_offer)
#     print(bid_info.objects.filter(pk=pk).highest_bid_user)
#     bid_info.objects.filter(pk=pk).save()
#     return render(request, "itemdetail.html", {'item': bid_info.objects.filter(pk=pk)})
