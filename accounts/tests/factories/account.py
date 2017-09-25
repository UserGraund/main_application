from __future__ import unicode_literals

import factory

from accounts.models import Account


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account
