from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import RoleEnum, User


class UserSerializer(ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(
        min_length=3,
        max_length=50,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Username must be from 3 to 50 characters long and can only contain letters, digits and underscores.",
            )
        ]
    )
    password = serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Password must be from 8 to 20 characters long and can only contain letters, digits and underscores.",
            )
        ]
    )
    first_name = serializers.CharField(
        min_length=1,
        max_length=100,
    )
    second_name = serializers.CharField(
        min_length=1,
        max_length=100,
        required=False,
        allow_blank=True,
    )
    last_name = serializers.CharField(
        min_length=1,
        max_length=100,
    )
    role = serializers.ChoiceField(
        choices=RoleEnum.choices(),
    )
    is_active = serializers.BooleanField(default=True)
    is_superuser = serializers.BooleanField(default=False)
    is_verified = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "second_name",
            "last_name",
            "role",
            "is_active",
            "is_superuser",
            "is_verified",
        )
