from __future__ import unicode_literals

from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created" and "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
