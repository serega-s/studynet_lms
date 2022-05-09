from django.urls import path

from activity import views

urlpatterns = [
    path('get_active_courses/', views.GetActiveCoursesListAPIView.as_view()),
    path('track_started/<slug:course_slug>/<slug:lesson_slug>/', views.TrackStartedAPIView.as_view()),
    path('mark_as_done/<slug:course_slug>/<slug:lesson_slug>/', views.MarkAsDoneAPIView.as_view())
]