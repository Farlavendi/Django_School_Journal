from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly, IsSuperUserOrReadOnly, IsOwnerOrReadOnly
from .models import Class, Student, Teacher
from .serializers import StudentSerializer, ClassSerializer, TeacherSerializer


class IsAdminViewSet(ModelViewSet):
    permission_classes = (
        IsAdminOrReadOnly,
    )
    pagination_class = LimitOffsetPagination


class IsSuperUserViewSet(ModelViewSet):
    permission_classes = (
        IsSuperUserOrReadOnly,
    )
    pagination_class = LimitOffsetPagination


class IsOwnerViewSet(ModelViewSet):
    permission_classes = (
        IsOwnerOrReadOnly,
    )
    pagination_class = LimitOffsetPagination


class StudentsViewSet(ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Student.objects.all()
        return Student.objects.select_related('_class').get(pk=pk)


class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Class.objects.all()
        return Class.objects.filter(pk=pk)


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Teacher.objects.all()
        return Teacher.objects.filter(pk=pk)