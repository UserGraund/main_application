from __future__ import unicode_literals

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from rest_framework.generics import (
    CreateAPIView
)

from accounts.api.serializers.account import (
    AccountRegisterSerializer,
    AccountLoginSerializer
)


class AccountRegisterViewSet(CreateAPIView):
    serializer_class = AccountRegisterSerializer
    permission_classes = (permissions.AllowAny,)


class AccountLoginViewSet(APIView):
    """
    Login view
    """
    serializer_class = AccountLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
