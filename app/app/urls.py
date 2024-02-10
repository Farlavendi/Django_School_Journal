from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('journal/', include("journal.urls")),
    path('admin/', admin.site.urls)
]
