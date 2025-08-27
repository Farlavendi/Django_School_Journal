from rest_framework.viewsets import ModelViewSet

from api.models import Class
from api.serializers.classes_serializers import (
    ClassCreateSerializer,
    ClassDetailSerializer,
    ClassListSerializer,
    ClassUpdateSerializer,
)


class ClassViewSet(ModelViewSet):
    permission_classes = []

    serializer_action_classes = {
        "create": ClassCreateSerializer,
        "list": ClassListSerializer,
        "retrieve": ClassDetailSerializer,
        "update": ClassUpdateSerializer,
        "partial_update": ClassUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Class.objects.all()
        return queryset
