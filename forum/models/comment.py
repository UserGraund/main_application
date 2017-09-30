from __future__ import unicode_literals

from django.db import models

from accounts.models import Account
from forum.models import TimeStampedModel, Post


class Comment(TimeStampedModel):
    content = models.TextField()

    post = models.ForeignKey(Post, related_name='comments')
    account = models.ForeignKey(Account, related_name='comments')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.account.username)
