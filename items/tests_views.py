from django.test import TestCase
# from django.shortcuts import get_object_or_404
from .models import Item
# from search_and_sort.views import sort_new, sort_price, sort_sold

# Create your tests here.


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/items/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
