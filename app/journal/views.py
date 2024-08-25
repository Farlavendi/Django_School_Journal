from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import Class, Student, Teacher
from .serializers import StudentSerializer


class StudentsAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
