from __future__ import unicode_literals

import factory

from accounts.tests.factories import AccountFactory
from forum.models import Post
from forum.tests.factories.forum_target import ForumTargetFactory


class PostFactory(factory.Factory):
    class Meta:
        model = Post

    account = factory.SubFactory(AccountFactory)
    forum_target = factory.SubFactory(ForumTargetFactory)
