from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from items.models import Item
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


# @login_required()
def payment(request, pk):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            # buyer_address = {
            #                  'name': order.full_name,
            #                  'street': order.street_address1,
            #                  'postcode': order.postcode,
            #                  'town': order.town_or_city,
            #                  'country': order.country
            #                 }
            item = get_object_or_404(Item, pk=pk)
            total = item.highest_bid_offer
            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid for this item")
                item.sold = 1
                item.buyer_name = order.full_name
                item.buyer_address = order.street_address1
                item.buyer_town = order.town_or_city
                item.buyer_postdoc = order.postcode
                item.buyer_country = order.country
                item.save()
                return render(request, "itemdetail.html", {'item': item})
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        print(id)
        item = get_object_or_404(Item, pk=pk)

    return render(request, "payment.html", {"item": item, "order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
