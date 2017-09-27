from __future__ import unicode_literals

from django.test import TestCase

from accounts.api.serializers.account import AccountSerializer
from accounts.tests.factories import AccountFactory


class AccountSerializerTestCase(TestCase):
    def setUp(self):
        super(AccountSerializerTestCase, self).setUp()

        self.account = AccountFactory()

    def test_serializer(self):
        """
        Account model serialized as excepted
        """

        result = AccountSerializer(instance=self.account)

        self.assertDictEqual(result.data, {
            'username': self.account.username,
            'email': self.account.email,
            'first_name': self.account.first_name,
            'last_name': self.account.last_name,
            'slug': self.account.slug
        })
