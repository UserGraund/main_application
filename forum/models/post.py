from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import Account
from forum.models import TimeStampedModel, ForumTarget


class Post(TimeStampedModel):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    content = models.TextField()

    forum_target = models.ForeignKey(ForumTarget, on_delete=models.CASCADE, related_name='posts')
    account = models.ForeignKey(Account, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)
