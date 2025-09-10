from django.core.validators import RegexValidator
from rest_framework import serializers

from api.models import Class, Student
from api.serializers.marks_serializers import MarksSerializer


class StudentCreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        min_length=2,
        max_length=3,
        validators=[
            RegexValidator(
                regex=r"^[1-9]\d?[A-Z]$",
                message="Code must be 1 or 2 digits (not starting with 0) followed by a capital letter (e.g., 1A, 12B).",
            )
        ],
        write_only=True,
    )

    class Meta:
        model = Student
        fields = ("code",)


class StudentListSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    class_code = serializers.CharField(source="_class.code")

    class Meta:
        model = Student
        fields = ("id", "user_id", "class_code")
        read_only_fields = ("id", "user_id", "class_code")


class StudentDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    class_code = serializers.CharField(source="_class.code")
    marks = MarksSerializer()

    class Meta:
        model = Student
        fields = ("id", "user_id", "class_code", "marks")
        read_only_fields = ("id", "user_id", "class_code", "marks")


class StudentUpdateSerializer(serializers.ModelSerializer):
    class_code = serializers.SlugRelatedField(
        slug_field="code",
        queryset=Class.objects.all(),
        source="_class",
        required=False,
    )

    class Meta:
        model = Student
        fields = ("class_code",)
