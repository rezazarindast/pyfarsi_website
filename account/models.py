from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=False)
    phone_number = PhoneNumberField(verbose_name='Phone Number', help_text='e.g: +98 ...')
    REQUIRED_FIELDS = ('password', 'email')

    class Meta:
        db_table = 'pyfarsi_users'
        ordering = ('-date_joined',)
