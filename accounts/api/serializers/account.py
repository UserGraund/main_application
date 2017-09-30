from __future__ import unicode_literals

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

Account = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class AccountRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    password = serializers.CharField(label='Password', write_only=True)
    password2 = serializers.CharField(label='Confirm password', write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password', 'password2', 'token')

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
            raise ValueError('passwords do not match')

        account = Account(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        account.set_password(password)
        account.save()

        payload = jwt_payload_handler(account)
        token = jwt_encode_handler(payload)

        validated_data['token'] = token

        return validated_data


class AccountLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, allow_blank=True)
    username = serializers.CharField()

    class Meta:
        model = Account
        fields = ('username', 'password', 'token')

    def validate(self, parameters):
        username = parameters['username']
        password = parameters['password']

        try:
            account = Account.objects.get(username=username, password=password)
        except (ValueError, Account.DoesNotExist):
            raise serializers.ValidationError('Incorrect credentials')

        payload = jwt_payload_handler(account)
        token = jwt_encode_handler(payload)

        parameters['token'] = token

        return parameters


class DefaultAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = fields
