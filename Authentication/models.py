from django.db import models
from django.http.response import FileResponse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, last_name, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, last_name, user_name, first_name, password,**other_fields)

    def create_user(self, email, last_name, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('you must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, last_name=last_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name

class VerificationCode(models.Model):
    typeOf = (
        ('R', 'Reset'),
        ('V', 'Verify')
    )
    code = models.IntegerField(null=True, blank=True)
    codeType = models.CharField(choices=typeOf, max_length=10)
    userId = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('userId', 'codeType')