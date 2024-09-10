from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.username
