from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (
        ("male", "남자"),
        ("female", "여자"),
    )
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
