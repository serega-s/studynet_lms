from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseListAPIView.as_view()),
    path('get-categories/', views.CategoryListAPIView.as_view()),
    path('get-author-courses/<int:user_id>/',
         views.AuthorCourseListAPIView.as_view()),
    path('create/', views.CreateCourseAPIView.as_view()),
    path('<slug:slug>/', views.GetCourseApiView.as_view()),
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/',
         views.GetQuizAPIView.as_view()),
    path('<slug:course_slug>/<slug:lesson_slug>/',
         views.AddCommentAPIView.as_view()),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/',
         views.GetCommentsAPIView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
