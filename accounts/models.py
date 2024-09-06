from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
