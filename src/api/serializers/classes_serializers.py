from django.core.validators import RegexValidator
from rest_framework import serializers

from api.models import Class
from api.serializers.students_serializers import StudentResponseSerializer
from api.serializers.teachers_serializers import TeacherResponseSerializer


class ClassCreateSerializer(serializers.ModelSerializer):
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
        model = Class
        fields = ("id", "code",)


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("id", "code")
        read_only_fields = ("id", "code")


class ClassDetailSerializer(serializers.ModelSerializer):
    students = StudentResponseSerializer(many=True, read_only=True)
    teacher = TeacherResponseSerializer(many=False, read_only=True)

    class Meta:
        model = Class
        fields = ("id", "code", "students", "teacher",)
        read_only_fields = ("id", "code", "students", "teacher",)


class ClassUpdateSerializer(serializers.ModelSerializer):
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
        model = Class
        fields = ("id", "code",)