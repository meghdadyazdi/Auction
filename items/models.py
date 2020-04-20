from django.db import models
from django.utils import timezone

# Create your models here.


class Item(models.Model):
    """
    A single item
    """
    title = models.CharField(max_length=200)
    seller = models.CharField(max_length=200, default='Active user')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    last_bid = models.IntegerField(default=0)
    timer = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __unicode__(self):
        return self.title
