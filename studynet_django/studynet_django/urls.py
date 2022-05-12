from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/courses/', include('course.urls')),
    path('api/v1/activities/', include('activity.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path(
        'openapi/', get_schema_view(
            title="StudyNet LMS",
            description="API for our LMS",
            version="1.0.0",
            permission_classes=[AllowAny],
        ), name='openapi-schema'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
