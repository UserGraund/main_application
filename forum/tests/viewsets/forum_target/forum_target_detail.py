from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from accounts.tests.factories import AccountFactory
from forum.models import ForumTarget

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ForumTargetDetailViewTestCase(APITestCase, TestCase):

    def setUp(self):
        super(ForumTargetDetailViewTestCase, self).setUp()

        self.account = AccountFactory()
        self.forum_target = ForumTarget.objects.create(
            account=self.account, name='Riki', description='test')

        self.token = jwt_encode_handler(jwt_payload_handler(self.account))
        self.client.force_login(self.account)

        self.url = reverse('forum_api:target-detail', kwargs={'pk': self.forum_target.id})

    def test_update_method(self):
        """
        User is authenticated, put valid data, forum target is updated
        """

        result = self.client.put(
            path=self.url,
            data=json.dumps({
                'name': 'test',
                'account': self.account.id,
                'description': self.forum_target.description
            }),
            HTTP_AUTHORIZATION='JWT {}'.format(self.token),
            content_type='application/json'
        )

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data['name'], 'test')

    def test_get_method(self):
        """
        Account try to get Forum Target, returned serialized data
        """
        result = self.client.get(path=self.url)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data['account'], self.account.id)
