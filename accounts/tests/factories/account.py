from __future__ import unicode_literals

from django.utils.text import slugify

import factory

from accounts.models import Account


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account

    username = factory.Sequence(lambda n: 'morty{}'.format(n))
    slug = factory.LazyAttribute(lambda o: slugify(o.username))
    password = factory.Faker('password')
    email = factory.LazyAttribute(lambda o: '{}@example.org'.format(o.username.lower()))
