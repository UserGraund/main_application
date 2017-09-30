from __future__ import unicode_literals

from rest_framework import serializers

from forum.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'account', 'id')
        ordering = ('created', )
