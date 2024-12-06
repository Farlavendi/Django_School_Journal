from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Journal API",
        default_version='v1',
        description="Documentation for school online api API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="example@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/session_auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger<format>/',
             schema_view.without_ui(cache_timeout=0),
             name='schema-json'
             ),
        path('swagger/',
             schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'
             ),
        path('redoc/',
             schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'
             ),
    ]  # + static(document_root=settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
