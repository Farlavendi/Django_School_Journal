from rest_framework.viewsets import ModelViewSet

from .models import Class, Student
from .serializers import StudentSerializer, ClassSerializer


class StudentsViewSet(ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Student.objects.all()
        return Student.objects.select_related('_class')


class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Class.objects.all()
        return Class.objects.filter(pk=pk)
