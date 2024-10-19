from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from permissions import IsAdminOrReadOnly
from .models import Class, Student
from .serializers import StudentSerializer, ClassSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes = (
        IsAdminOrReadOnly,
    )
    pagination_class = LimitOffsetPagination


class StudentsViewSet(ProjectViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Student.objects.all()
        return Student.objects.select_related('_class')


class ClassViewSet(ProjectViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Class.objects.all()
        return Class.objects.filter(pk=pk)
