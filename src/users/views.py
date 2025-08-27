from django.db import transaction
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Class, Marks, Student, Teacher
from .models import User
from .serializers import (
    StudentUserCreateSerializer,
    TeacherUserCreateSerializer,
    UserResponseSerializer,
    UserUpdateSerializer
)


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = []

    serializer_action_classes = {
        "list": UserResponseSerializer,
        "retrieve": UserResponseSerializer,
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
        "create_student": StudentUserCreateSerializer,
        "create_teacher": TeacherUserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    @action(detail=False, methods=["post"], url_path="register/student")
    def create_student(self, request):
        serializer = StudentUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create(**serializer.validated_data["user"])

            _class = get_object_or_404(
                Class,
                code=serializer.validated_data["code"]
            )

            student = Student.objects.create(
                user=user,
                _class=_class,
            )

            Marks.objects.create(student=student)

        return Response(
            data=UserResponseSerializer(user).data,
            status=201,
        )

    @action(detail=False, methods=["post"], url_path="register/teacher")
    def create_teacher(self, request):
        serializer = TeacherUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create(**serializer.validated_data["user"])

            _class = get_object_or_404(
                Class,
                code=serializer.validated_data["code"]
            )

            Teacher.objects.create(
                user=user,
                subject=serializer.validated_data["subject"],
                _class=_class,
            )

        return Response(
            UserResponseSerializer(user).data,
            status=201,
        )
