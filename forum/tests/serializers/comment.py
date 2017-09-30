from __future__ import unicode_literals

from django.test import TestCase

from forum.api.serializers.comment import CommentSerializer
from forum.tests.factories import CommentFactory


class CommentSerializerTestCase(TestCase):

    def setUp(self):
        super(CommentSerializerTestCase, self).setUp()

        self.comment = CommentFactory()

    def test_serialize_success(self):
        """
        Post object serialized success
        """
        result = CommentSerializer(self.comment)

        self.assertDictEqual(result.data, {
            'id': self.comment.id,
            'account': self.comment.account.id,
            'post': self.comment.post.id,
            'content': self.comment.content,
            'created': self.comment.created,
            'modified': self.comment.modified
        })
