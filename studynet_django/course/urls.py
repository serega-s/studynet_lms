from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.get_courses),
    path('get-categories/', views.get_categories),
    path('get-frontpage-courses/', views.get_frontpage_courses),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', views.get_comments),
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/', views.get_quiz),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
