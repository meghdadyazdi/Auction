from django.test import TestCase
from .forms import OrderForm, MakePaymentForm
# Create your tests here.


class TestToDoOrderForm(TestCase):

    def test_can_creat_an_Order(self):
        form = OrderForm({'full_name' : 'Meghdad Y', 'phone_number': '0046 88888888', 'country': "Sweden",
            'town_or_city': 'Lund', 'street_address1': 'Ave. 1',
            'county': 'Skane'})
        self.assertTrue(form.is_valid())

    def test_error(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])

# class TestToDoOrderForm(TestCase):

#     def test_can_creat_an_MakePaymentForm(self):
#         form = MakePaymentForm({'credit_card_number' : '4242424242424242', 'cvv': '111', 'expiry_month': '1',
#             'expiry_year': '2035'})
#         self.assertTrue(form.is_valid())

    # def test_error(self):
    #     form = MakePaymentForm({'full_name': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['full_name'], [u'This field is required.'])
