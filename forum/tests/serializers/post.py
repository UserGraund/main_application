from __future__ import unicode_literals

from django.test import TestCase

from forum.api.serializers.post import PostSerializer
from forum.tests.factories import PostFactory


class PostSerializerTestCase(TestCase):

    def setUp(self):
        super(PostSerializerTestCase, self).setUp()

        self.post = PostFactory()

    def test_serialize_success(self):
        """
        Post object serialized success
        """
        result = PostSerializer(self.post)

        self.assertDictEqual(result.data, {
            'id': self.post.id,
            'title': self.post.title,
            'slug': self.post.slug,
            'account': self.post.account.id,
            'forum_target': self.post.forum_target.id,
            'content': self.post.content,
            'created': self.post.created,
            'modified': self.post.modified
        })
