from __future__ import unicode_literals

from django.test import TestCase

from rest_framework.serializers import ValidationError

from accounts.api.serializers.account import AccountLoginSerializer
from accounts.tests.factories import AccountFactory


class AccountLoginSerializerTestCase(TestCase):
    def setUp(self):
        super(AccountLoginSerializerTestCase, self).setUp()

        self.account = AccountFactory(username='bimbo')

        self.serializer = AccountLoginSerializer()
        self.login_data = {
            'username': self.account.username,
            'password': self.account.password
        }

    def test_serializer_login_validate_success(self):
        """
        Account login serializer validate method success, token generated
        """
        result = self.serializer.validate(parameters=self.login_data)

        self.assertIsNotNone(result['token'])

    def test_serializer_login_validate_failed(self):
        """
        Account login serializer validate method failed, Account is not exists in DB
        """
        with self.assertRaises(ValidationError):
            self.serializer.validate(parameters={
                'username': 'test',
                'password': 'test'
            })
