from __future__ import unicode_literals

import factory

from accounts.tests.factories import AccountFactory
from forum.models import Comment
from forum.tests.factories.post import PostFactory


class CommentFactory(factory.Factory):
    class Meta:
        model = Comment

    account = factory.SubFactory(AccountFactory)
    post = factory.SubFactory(PostFactory)
