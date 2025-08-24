from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Teacher
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
    queryset = Teacher.objects.all()
    permission_classes = []

    serializer_action_classes = {
        "list": TeacherResponseSerializer,
        "retrieve": TeacherResponseSerializer,
        "update": TeacherUpdateSerializer,
        "partial_update": TeacherUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)
