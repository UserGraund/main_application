from __future__ import unicode_literals

from django.contrib import admin

from forum.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
