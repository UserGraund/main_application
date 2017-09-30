from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import permissions

from forum.models import Post
from forum.api.serializers.post import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
