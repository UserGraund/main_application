from __future__ import unicode_literals

from django.contrib import admin

from forum.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
