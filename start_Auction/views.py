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
    print(item.auction_end_time)
    print(item.auction_duration_time)
    item.save()
    return render(request, "itemdetail.html", {'item': item})
