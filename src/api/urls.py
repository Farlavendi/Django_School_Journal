from django.urls import include, path
from rest_framework import routers

from .views import StudentsViewSet, ClassViewSet, TeacherViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"students", StudentsViewSet, basename="students")
router.register(r"classes", ClassViewSet, basename="classes")
router.register(r"teachers", TeacherViewSet, basename="teachers")

urlpatterns = [
    path("", include(router.urls)),
]
