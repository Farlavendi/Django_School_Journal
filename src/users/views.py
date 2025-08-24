from django.contrib.auth.hashers import make_password
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Student, Teacher
from api.serializers.students_serializers import StudentResponseSerializer
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

    @action(detail=False, methods=["post"], url_path="register/student")
    def create_student(self, request):
        serializer = StudentUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = {
            "email": serializer.validated_data["email"],
            "username": serializer.validated_data["username"],
            "role": RoleEnum.STUDENT,
            "password": make_password(serializer.validated_data["password"]),
            "first_name": serializer.validated_data["first_name"],
            "second_name": serializer.validated_data.get("second_name"),
            "last_name": serializer.validated_data["last_name"],
        }
        print(serializer.validated_data)
        print(serializer.validated_data["username"])
        user = User.objects.create(**user_data)

        student_data = {
            "user": user,
            "class_id": serializer.validated_data["class_id"],
        }

        student = Student.objects.create(**student_data)

        return Response(
            data = [
            UserResponseSerializer(user).data,
            StudentResponseSerializer(student).data
            ],
            status=201
        )

    @action(detail=False, methods=["post"], url_path="register/teacher")
    def create_teacher(self, request):
        serializer = TeacherUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            role=RoleEnum.TEACHER,
            password=make_password(serializer.validated_data["password"]),
        )
        Teacher.objects.create(user=user, **serializer.validated_data["teacher_extra"])

        return Response(UserResponseSerializer(user).data, status=201)

