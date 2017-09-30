from __future__ import unicode_literals

from rest_framework import routers

from accounts.api.viewsets import account


router = routers.DefaultRouter()
router.register(r'register', account.AccountRegisterViewSet.as_view(), base_name='account_register')
router.register(r'login', account.AccountLoginViewSet.as_view(), base_name='account_login')

urlpatterns = router.urls
