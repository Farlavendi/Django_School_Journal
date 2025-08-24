__all__ = [
    "ClassViewSet",
    "StudentsViewSet",
    "TeacherViewSet"
]

from .students_views import StudentsViewSet
from .teachers_views import TeacherViewSet
from .classes_views import ClassViewSet