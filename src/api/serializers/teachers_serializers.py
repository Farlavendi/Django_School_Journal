from rest_framework import serializers

from api.models import SubjectEnum, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subject = serializers.ChoiceField(choices=SubjectEnum.choices())

    class Meta:
        model = Teacher
        fields = ( "user", "_class", "subject")