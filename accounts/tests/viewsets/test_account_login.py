from __future__ import unicode_literals

import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from accounts.api.serializers.account import AccountLoginSerializer
from accounts.tests.factories import AccountFactory
from accounts.api.viewsets.account import AccountLoginViewSet


class AccountLoginPostTestCase(TestCase):
    def setUp(self):
        super(AccountLoginPostTestCase, self).setUp()

        self.serializer = AccountLoginSerializer()
        self.account = AccountFactory()
        self.request_factory = APIRequestFactory()

    def test_login_account_success(self):
        """
        Account login success when user put right data
        """

        view = AccountLoginViewSet.as_view()

        result = view(self.request_factory.post(
            path='/api/accounts/login',
            data=json.dumps({
                'username': self.account.username,
                'password': self.account.password
            }),
            content_type='application/json'
        ))

        self.assertEqual(result.status_code, 200)

    def test_login_account_failed(self):
        """
        Account login failed when user put invalid data
        """
        view = AccountLoginViewSet.as_view()

        result = view(self.request_factory.post(
            path='/api/accounts/login',
            data=json.dumps({
                'username': self.account.username,
                'password': self.account.password + '123'
            }),
            content_type='application/json'
        ))

        self.assertEqual(result.status_code, 400)
