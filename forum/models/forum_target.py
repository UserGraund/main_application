from __future__ import unicode_literals

from django.db import models

from accounts.models import Account
from forum.models import TimeStampedModel


class ForumTarget(TimeStampedModel):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    account = models.ForeignKey(Account, related_name='forum_targets')

    class Meta:
        verbose_name = 'Forum target'
        verbose_name_plural = 'Forum targets'

    def __str__(self):
        return self.name
