from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Class, Student, Teacher
from .models import RoleEnum, User
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
    queryset = User.objects.all()
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
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"], url_path="register/student")
    def create_student(self, request):
        serializer = StudentUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create(
                email=serializer.validated_data["email"],
                username=serializer.validated_data["username"],
                role=RoleEnum.STUDENT,
                password=make_password(serializer.validated_data["password"]),
                first_name=serializer.validated_data["first_name"],
                second_name=serializer.validated_data.get("second_name"),
                last_name=serializer.validated_data["last_name"],
            )

            _class = get_object_or_404(
                Class,
                serializer.validated_data["code"]
            )

            Student.objects.create(
                user=user,
                _class=_class,
            )

        return Response(
            data=UserResponseSerializer(user).data,
            status=201,
        )

    @action(detail=False, methods=["post"], url_path="register/teacher")
    def create_teacher(self, request):
        serializer = TeacherUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create(
                email=serializer.validated_data["email"],
                username=serializer.validated_data["username"],
                role=RoleEnum.STUDENT,
                password=make_password(serializer.validated_data["password"]),
                first_name=serializer.validated_data["first_name"],
                second_name=serializer.validated_data.get("second_name"),
                last_name=serializer.validated_data["last_name"],
            )

            _class = get_object_or_404(
                Class,
                serializer.validated_data["code"]
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
