from django.core.validators import RegexValidator
from rest_framework import serializers
from api.models import Class


class ClassSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
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

    students = StudentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Class
        fields = ("code", "students", "teacher", "user")