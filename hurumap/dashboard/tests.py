from __future__ import print_function
from django.core.urlresolvers import resolve
from django.test import TestCase


class AuthenticationTest(TestCase):
    def test_login_endpoint_exists(self):
        found = resolve('/accounts/login/')
        print(found)
        self.assertEqual(found.view_name, 'account_login')

    def test_signup_endpoint_exists(self):
        found = resolve('/accounts/signup/')
        print(found)
        self.assertEqual(found.view_name, 'account_signup')
