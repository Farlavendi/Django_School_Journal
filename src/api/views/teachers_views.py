from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Student, Teacher
from api.serializers.marks_serializers import MarksSerializer, MarksUpdateSerializer
from api.serializers.teachers_serializers import (
    TeacherResponseSerializer,
    TeacherUpdateSerializer,
)


class TeacherViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = []

    serializer_action_classes = {
        "list": TeacherResponseSerializer,
        "retrieve": TeacherResponseSerializer,
        "update": TeacherUpdateSerializer,
        "partial_update": TeacherUpdateSerializer,
        "update_marks": MarksUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

    @action(detail=False, methods=["put"], url_path="update_marks/(?P<student_id>[^/.]+)")
    def update_marks(self, request, student_id=None):
        student = Student.objects.filter(id=student_id).first()
        if not student:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        if not hasattr(student, "marks") or student.marks is None:
            return Response({"detail": "Student has no marks record"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarksSerializer(student.marks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)