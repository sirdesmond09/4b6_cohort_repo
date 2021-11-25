from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# from subscription.models import Plan

class User(AbstractUser):
    

    def __str__(self):
        return self.username


