from __future__ import unicode_literals

from rest_framework import routers

from forum.api.viewsets.post import PostViewSet
from forum.api.viewsets.comment import CommentViewSet
from forum.api.viewsets.forum_target import ForumTargetViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, base_name='post')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'target', ForumTargetViewSet, base_name='target')

urlpatterns = router.urls
