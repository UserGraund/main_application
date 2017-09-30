from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import permissions

from forum.api.serializers.comment import CommentSerializer
from forum.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
