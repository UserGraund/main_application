from __future__ import unicode_literals

import factory

from accounts.tests.factories import AccountFactory
from forum.models import ForumTarget


class ForumTargetFactory(factory.Factory):
    class Meta:
        model = ForumTarget

    name = factory.Sequence(lambda n: 'Rick{}'.format(n))
    account = factory.SubFactory(AccountFactory)
    description = factory.Sequence(lambda n: 'Lool{}'.format(n))
