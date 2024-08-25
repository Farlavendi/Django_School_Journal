from rest_framework import serializers

from journal.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', '_class')
