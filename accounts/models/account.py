from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils import timezone


class AccountManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates user
        :param username: str
        :param email: str, email field
        :param password: str
        :param extra_fields: additional information about user
        :return: created account
        """

        if not username:
            raise ValueError('Username is required parameter')

        if not password:
            raise ValueError('Password is required parameter')

        email = self.normalize_email(email)
        account = self.model(
            username=username,
            email=email,
            is_active=True,
            date_joined=timezone.now(),
            **extra_fields
        )
        account.set_password(password)
        account.save()

        return account

    def create_user(self, username, password, email=None, **extra_fields):
        """
        Creates default account
        :param username: str
        :param email: str, email field
        :param password: str
        :param extra_fields: additional information about user
        """

        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            username=username,
            password=password,
            email=email,
            **extra_fields
        )

    def create_superuser(self, username, password, email=None, **extra_fields):
        """
        Creates superuser of system
        :param username: str
        :param email: str, email field
        :param password: str
        :param extra_fields: additional information about user
        """
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(
            username=username,
            password=password,
            email=email,
            **extra_fields
        )


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Account model
    """

    object = AccountManager()

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    slug = models.SlugField(max_length=50)

    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)

        super(Account, self).save(*args, **kwargs)
