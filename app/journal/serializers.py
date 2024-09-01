from rest_framework import serializers

from journal.models import Student, Class, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', '_class')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', '_class')


class ClassSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Class
        fields = ('number', 'teacher', 'students')