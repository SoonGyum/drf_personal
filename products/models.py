from django.db import models
from accounts.models import User

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


# class Product(models.Model):
#     CATEGORY_CHOICES = (
#         ("F", "Fruit"),
#         ("V", "Vegetable"),
#         ("M", "Meat"),
#         ("O", "Other"),
#     )
#     name = models.CharField(max_length=30)
#     price = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField()
#     category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
