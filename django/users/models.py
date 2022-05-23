from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import random
import string

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'is_superuser=True')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('이메일 주소를 입력해야합니다.'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    account_address = models.BigIntegerField(_('account address'), unique=True, default=''.join(random.choice(string.digits) for _ in range(8)))
    account_money = models.BigIntegerField(_('account money'), default=0)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name#,str(self.account_money)

class TransferReport(models.Model):
    send_account = models.BigIntegerField(_('send account'))
    receive_account = models.BigIntegerField(_('receive account'))
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
