from rest_framework import serializers

from .models import Marks, Student, Class, SubjectEnum, Teacher


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = ("user", "_class")


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subject = serializers.ChoiceField(choices=SubjectEnum.choices())

    class Meta:
        model = Teacher
        fields = ( "user", "_class", "subject")


class ClassSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    students = StudentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Class
        fields = ("number", "students", "teacher", "user")

class MarksSerializer(serializers.ModelSerializer):
    maths = serializers.CharField(allow_blank=True)
    english = serializers.CharField(allow_blank=True)
    physics = serializers.CharField(allow_blank=True)
    chemistry = serializers.CharField(allow_blank=True)
    history = serializers.CharField(allow_blank=True)
    geography = serializers.CharField(allow_blank=True)
    literature = serializers.CharField(allow_blank=True)

    class Meta:
        model = Marks
        fields = ("maths", "english", "physics", "chemistry", "history", "geography", "literature")