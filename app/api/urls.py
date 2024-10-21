from django.urls import include, path
from rest_framework import routers

from .views import StudentsViewSet, ClassViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')
router.register(r'classes', ClassViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls)),
]