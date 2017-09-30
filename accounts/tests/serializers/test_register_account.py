from __future__ import unicode_literals

from django.test import TestCase

from accounts.api.serializers.account import AccountRegisterSerializer


class AccountRegisterSerializerTestCase(TestCase):
    def setUp(self):
        super(AccountRegisterSerializerTestCase, self).setUp()

        self.register_data = {
            'username': 'test',
            'password': '123',
            'password2': '123',
            'email': 'test@gmail.com'
        }

        self.serializer = AccountRegisterSerializer()

    def test_register_serializer_create_failed(self):
        """
        Account register serializer create method failed passwords do not match
        """
        self.register_data['password2'] = '124'

        with self.assertRaises(ValueError):
            self.serializer.create(validated_data=self.register_data)

    def test_register_serializer_create_success_token_generated(self):
        """
        Account register serializer create method success, token generated
        """
        result = self.serializer.create(validated_data=self.register_data)

        self.assertIsNotNone(result['token'])
