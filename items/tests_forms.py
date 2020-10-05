from django.test import TestCase
from items.forms import ItemForm
# Create your tests here.


class TestToDoItemForm(TestCase):

    def test_can_creat_an_item_with_title_and_price(self):
        form = ItemForm({'title': 'New', 'price': 1})
        # print('##################')
        # print(form.is_valid())
        # print('##################')
        self.assertTrue(form.is_valid())

    def test_error(self):
        form = ItemForm({'title': '', 'price': 1})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

