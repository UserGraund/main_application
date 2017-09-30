from __future__ import unicode_literals

from django.test import TestCase

from forum.api.serializers.forum_target import ForumTargetSerializer
from forum.tests.factories.forum_target import ForumTargetFactory


class ForumTargetSerializerTestCase(TestCase):

    def setUp(self):
        super(ForumTargetSerializerTestCase, self).setUp()

        self.forum_target = ForumTargetFactory()

    def test_serialize_success(self):
        """
        ForumTarget object serialized success
        """
        result = ForumTargetSerializer(self.forum_target)

        self.assertDictEqual(result.data, {
            'id': self.forum_target.id,
            'name': self.forum_target.name,
            'account': self.forum_target.account.id,
            'description': self.forum_target.description,
            'created': self.forum_target.created,
            'modified': self.forum_target.modified
        })
