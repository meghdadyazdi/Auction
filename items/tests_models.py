from django.test import TestCase
from .models import Item, bid_info

# Create your tests here.


class TestItemModel(TestCase):

    def test_can_create_an_item_with_a_titele_description(self):
        item = Item(title="Create a Test", description='New Item')
        item.save()
        self.assertEqual(item.title, "Create a Test")

    def test_item_as_a_string(self):
        item = Item(title="Create a Test")
        print(str(item))
        self.assertEqual("Create a Test", str(item))


class TestBid_infoModel(TestCase):

    def test_can_create_a_bid_with_highest_bid(self):
        bid = bid_info(highest_bid_user="admin", highest_bid_offer='50')
        bid.save()
        self.assertEqual(bid.highest_bid_user, "admin")
