from __future__ import unicode_literals

from rest_framework import viewsets, permissions

from forum.api.serializers.forum_target import ForumTargetSerializer
from forum.models import ForumTarget


class ForumTargetViewSet(viewsets.ModelViewSet):
    queryset = ForumTarget.objects.all()
    serializer_class = ForumTargetSerializer
    permissions = (permissions.AllowAny, )

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
