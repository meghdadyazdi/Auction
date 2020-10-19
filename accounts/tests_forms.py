from django.test import TestCase
from .forms import UserRegistrationForm
# Create your tests here.


class TestToDoItemForm(TestCase):

    def test_can_creat_an_UserRegistrationForm(self):
        form = UserRegistrationForm({'username': 'New', 'email': 'new@website.com', 'password1': '@123', 'password2': '@123'})
        self.assertTrue(form.is_valid())

    def test_error(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

