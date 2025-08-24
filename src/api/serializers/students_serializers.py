from django.core.validators import RegexValidator
from rest_framework import serializers

from api.models import Student


class StudentCreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        min_length=2,
        max_length=3,
        validators=[
            RegexValidator(
                regex=r"^\d{1,2}[A-Z]$",
                message="Code must be 1 or 2 digits followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
    )

    class Meta:
        model = Student
        fields = ("code",)


class StudentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    code = serializers.CharField(
        min_length=2,
        max_length=3,
        validators=[
            RegexValidator(
                regex=r"^\d{1,2}[A-Z]$",
                message="Code must be 1 or 2 digits followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
        required=False,
    )

    class Meta:
        model = Student
        fields = ("id", "code",)


class StudentResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    class_code = serializers.CharField(source="_class.code")

    class Meta:
        model = Student
        fields = ("id", "user_id", "class_code")
        read_only_fields = ("id", "user_id", "class_code")
