from rest_framework import serializers

from .models import Student, Class, Teacher


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = ('name', '_class', 'user')


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Teacher
        fields = ('name', '_class', 'user')


class ClassSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    students = StudentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Class
        fields = ('number', 'students', 'teacher', 'user')
