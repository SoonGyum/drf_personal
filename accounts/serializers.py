from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            name=validated_data["name"],
            nickname=validated_data["nickname"],
            email=validated_data["email"],
            birthday=validated_data["birthday"],
            gender=validated_data["gender"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
