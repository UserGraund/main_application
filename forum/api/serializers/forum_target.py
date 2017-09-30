from __future__ import unicode_literals

from rest_framework import serializers

from forum.models import ForumTarget


class ForumTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumTarget
        fields = '__all__'
