from django.core.validators import RegexValidator
from rest_framework import serializers

from api.models import SubjectEnum, Teacher


class TeacherCreateSerializer(serializers.ModelSerializer):
    subject = serializers.ChoiceField(choices=SubjectEnum.choices())
    # TODO check maybe move to just a pos arg to have nice drop-list
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
        model = Teacher
        fields = ("subject", "code", )


class TeacherUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    subject = serializers.ChoiceField(
        choices=SubjectEnum.choices(),
        required=False,
    )
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
        model = Teacher
        fields = ("id", "subject", "code", )


class TeacherResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    class_code = serializers.CharField(source="_class.code")

    class Meta:
        model = Teacher
        fields = ("id", "user_id", "class_code", "subject")
        read_only_fields = ("id", "user_id", "class_code", "subject")