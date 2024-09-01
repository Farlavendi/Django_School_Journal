from rest_framework.viewsets import ModelViewSet

from .models import Class, Student, Teacher
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
        print(
            Teacher.objects.filter(_class=pk).values_list('name'),
            Student.objects.filter(_class=pk).values_list('name'),
        )
        return Class.objects.filter(pk=pk)

#
# class TeacherViewSet(ModelViewSet):
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Teacher.objects.all()
