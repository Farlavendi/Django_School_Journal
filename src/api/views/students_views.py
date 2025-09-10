from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Student
from api.serializers.marks_serializers import MarksSerializer
from api.serializers.students_serializers import (
    StudentDetailSerializer,
    StudentListSerializer,
    StudentUpdateSerializer,
)


class StudentsViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = []

    serializer_action_classes = {
        "list": StudentListSerializer,
        "retrieve": StudentDetailSerializer,
        "update": StudentUpdateSerializer,
        "partial_update": StudentUpdateSerializer,
        "get_marks": MarksSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

    @action(detail=True, methods=["get"])
    def get_marks(self):
        student = self.get_object()
        if not hasattr(student, "marks") or student.marks is None:
            return Response({"detail": "No marks found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarksSerializer(student.marks)
        return Response(serializer.data)
