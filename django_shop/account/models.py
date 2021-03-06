import re

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



def validate_phone(value):
    if not bool(re.match('(09\d{9})', value)) or len(value) != 11:
        raise ValidationError('شماره موبایل وارد شده غیر مجاز است.')
    return value


class User(AbstractUser):
    """
    Custom User model. Email & Phone as identifier
    """
    username = None
    email = models.EmailField('ایمیل', max_length=254, unique=True)
    phone = models.CharField('شماره موبایل', max_length=11, unique=True, validators=[validate_phone])
    avatar = models.ImageField('تصویر پروفایل', upload_to='avatar', blank=True, default="defaultavatar.png")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
