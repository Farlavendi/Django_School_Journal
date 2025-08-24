from django.urls import include, path
from rest_framework import routers

from users.views import UserViewSet
from .views import ClassViewSet, StudentsViewSet, TeacherViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"students", StudentsViewSet, basename="students")
router.register(r"classes", ClassViewSet, basename="classes")
router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
