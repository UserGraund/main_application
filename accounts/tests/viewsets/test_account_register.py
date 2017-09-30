from __future__ import unicode_literals

import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from accounts.tests.factories import AccountFactory
from accounts.api.serializers.account import AccountRegisterSerializer
from accounts.api.viewsets.account import AccountRegisterViewSet


class AccountRegisterTestCase(TestCase):
    def setUp(self):
        super(AccountRegisterTestCase, self).setUp()

        self.serializer = AccountRegisterSerializer()
        self.request_factory = APIRequestFactory()
        self.view = AccountRegisterViewSet().as_view()

    def test_account_register_success(self):
        """
        User put right data, account was created
        """
        result = self.view(self.request_factory.post(
            path='/api/v1/register',
            data=json.dumps({
                'username': 'test',
                'password': '123',
                'password2': '123',
                'email': 'test@gmail.com'
            }),
            content_type='application/json'
        ))

        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.data['username'], 'test'),
        self.assertIsNotNone(result.data['token'])

    def test_account_register_failed_password_mismatch(self):
        """
        User put two different passwords, raised ValueError
        """
        with self.assertRaises(ValueError) as e:
            self.view(self.request_factory.post(
                path='/api/v1/register',
                data=json.dumps({
                    'username': 'test',
                    'password': '123',
                    'password2': '124',
                    'email': 'test@gmail.com'
                }),
                content_type='application/json'
            ))

        self.assertEqual(e.exception.args[0], 'passwords do not match')

    def test_account_register_failed_but_account_is_created(self):
        """
        User try to create account with username which already exists, account wasn not created
        """
        AccountFactory(username='test')

        result = self.view(self.request_factory.post(
            path='/api/v1/register',
            data=json.dumps({
                'username': 'test',
                'password': '123',
                'password2': '124',
                'email': 'test@gmail.com'
            }),
            content_type='application/json'
        ))

        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.data['username'][0], 'Account with this username already exists.')
