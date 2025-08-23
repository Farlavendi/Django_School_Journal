from django.core.validators import RegexValidator
from rest_framework import serializers
from api.models import Student


class BaseStudentSerializer(serializers.ModelSerializer):
    class_id = serializers.UUIDField(source="_class.id")

    class Meta:
        model = Student
        fields = ("class_id",)


class StudentCreateSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        min_length=2,
        max_length=3,
        validators=[
            RegexValidator(
                regex=r"^\d{1,2}[A-Z]$",
                message="Class number must be 1 or 2 digits followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
    )

    class Meta:
        model = Student
        fields = ("_class", "number")

    def validate_number(self, value):
        # Optional: normalize input to uppercase
        return value.upper()


class StudentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    number = serializers.CharField(
        min_length=2,
        max_length=3,
        required=False,
        validators=[
            RegexValidator(
                regex=r"^\d{1,2}[A-Z]$",
                message="Class number must be 1 or 2 digits followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
    )

    class Meta:
        model = Student
        fields = ("id", "number")


class StudentResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    class_number = serializers.CharField(source="_class.number")

    class Meta:
        model = Student
        fields = ("id", "user_id", "class_number")
