from django.contrib import admin
from django.urls import path, include

from journal.views import StudentsAPIView

urlpatterns = [
    path('', include("journal.urls")),
    path('journal/', include("journal.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/student_list/', StudentsAPIView.as_view()),
]
