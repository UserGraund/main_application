from __future__ import unicode_literals

from django.contrib import admin

from forum.models import ForumTarget


@admin.register(ForumTarget)
class ForumTargetAdmin(admin.ModelAdmin):
    pass
