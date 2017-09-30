from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from forum.models import ForumTarget
from accounts.tests.factories import AccountFactory

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ForumTargetListViewTestCase(APITestCase):
    url = reverse('forum_api:target-list')

    def setUp(self):
        super(ForumTargetListViewTestCase, self).setUp()

        self.account = AccountFactory()

        self.token = jwt_encode_handler(jwt_payload_handler(self.account))
        self.client.force_login(self.account)

    def test_create_method(self):
        """
        User is authenticated, put valid data, forum target is created
        """

        result = self.client.post(
            path=self.url,
            data=json.dumps({
                'name': 'test',
                'description': 'testing',
                'account': self.account.id
            }),
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            content_type='application/json'
        )

        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.data['name'], 'test')

    def test_get_method(self):
        """
        Account try to get list of Forum Targets, returned serialized data
        """
        ForumTarget.objects.create(account=self.account)

        result = self.client.get(path=self.url)

        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.data['count'], 0)
