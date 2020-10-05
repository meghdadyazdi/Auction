from django.db import models
from django.utils import timezone

# Create your models here.


class Item(models.Model):
    """
    A single item
    """
    title = models.CharField(max_length=200, blank=False)
    seller = models.CharField(max_length=200, default='Active user')
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    price = models.PositiveIntegerField(default=1, null=True)
    highest_bid_user = models.CharField(default="", max_length=200)
    highest_bid_offer = models.IntegerField(default=0)
    auction_status = models.IntegerField(default=0)
    auction_end_time = models.IntegerField(default=0, null=True)
    auction_duration_time = models.IntegerField(default=0, null=True)
    sold = models.IntegerField(default=0)
    endtime = models.IntegerField(default=0)
    buyer_name = models.CharField(max_length=30, default=0, blank=False, null=False)
    buyer_address = models.CharField(max_length=30, default=0, blank=False, null=False)
    buyer_town = models.CharField(max_length=30, default=0, blank=False, null=False)
    buyer_postcode = models.CharField(max_length=30, default=0, blank=False, null=False)
    buyer_country = models.CharField(max_length=30, default=0, blank=False, null=False)
    comment_seller = models.TextField(default="No comment yet")
    comment_winner = models.TextField(default="No comment yet")
    timer = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __unicode__(self):
        return self.title


class bid_info(models.Model):
    """
    Information related to the bidders
    """
    highest_bid_user = models.CharField(default="a", max_length=200)
    highest_bid_offer = models.IntegerField(default=0)

    def __unicode__(self):
        return self.highest_bid_user
