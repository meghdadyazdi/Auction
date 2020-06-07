from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from payment.models import Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def get_items(request):
    """
    Return a list of items that are added by sellers
    and render them to the 'index.html' template.
    """
    items = Item.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    paginator = Paginator(items, 5)
    page = request.GET.get('page', 1)
    items = paginator.page(page)
    return render(request, "index.html", {'items': items, "mode": 'all'})


def item_detail(request, pk):
    """
    Returns a single item based on the item ID (pk) and
    render it to the 'itemdetail.html' template.
    Or return a 404 error if the item is
    not found
    """
    item = get_object_or_404(Item, pk=pk)
    item.views += 1
    item.save()
    return render(request, "itemdetail.html", {'item': item})


def restart_auction(request, pk):
    """
    Returns a single item based on the item ID (pk) and
    render it to the 'itemdetail.html' template.
    Or return a 404 error if the item is
    not found
    """
    item = get_object_or_404(Item, pk=pk)
    item.auction_status = 0
    item.save()
    return render(request, "itemdetail.html", {'item': item})


@login_required
def add_or_edit_item(request, pk=None):
    """
    Add or edit an item depending if the item ID
    is null or not
    Only loged in users can add item
    Only the creator can edit the item.
    Creator can not edit after auction starts
    """
    # pk if you are editing, No pk if you are adding
    item = get_object_or_404(Item, pk=pk) if pk else None
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            item.seller = request.user.username
            item.save()
            return redirect(item_detail, item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'itemform.html', {'form': form})
