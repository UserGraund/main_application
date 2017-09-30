from __future__ import unicode_literals

from rest_framework import serializers

from forum.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        ordering = ('created', )
