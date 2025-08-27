from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Student
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
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset
