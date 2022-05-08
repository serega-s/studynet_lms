from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Category, Comment, Course, Lesson
from course.serializers import (
    CategorySerializer, CommentSerializer,
    CourseDetailSerializer, CourseListSerializer,
    LessonListSerializer, QuizSerializer
)


class GetQuizAPIView(APIView):
    def get(self, request, course_slug, lesson_slug):
        lesson = Lesson.objects.get(slug=lesson_slug)
        quiz = lesson.quizzes.first()
        serializer = QuizSerializer(quiz)

        return Response(serializer.data)


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    authentication_classes = []


class GetCourseApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        course_serializer = CourseDetailSerializer(course)
        lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

        if request.user.is_authenticated:
            course_data = course_serializer.data
        else:
            course_data = {}

        return Response(
            {
                'course': course_data,
                'lessons': lesson_serializer.data
            }
        )


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all().prefetch_related('categories').order_by('-created_at')
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = CourseListSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = super().get_queryset()
        if category_id:
            queryset = queryset.filter(categories__in=[int(category_id)])

        limit = self.request.query_params.get('limit')
        if limit:
            queryset = queryset[:int(limit)]

        return queryset


class GetCommentsAPIView(APIView):
    def get(self, request, course_slug, lesson_slug):
        lesson = Lesson.objects.get(slug=lesson_slug)
        serializer = CommentSerializer(lesson.comments.all(), many=True)
        return Response(serializer.data)


class AddCommentAPIView(APIView):
    def post(self, request, course_slug, lesson_slug):
        data = request.data
        name = data['name']
        content = data['content']
        course = Course.objects.get(slug=course_slug)
        lesson = Lesson.objects.get(slug=lesson_slug)

        comment = Comment.objects.create(
            course=course, lesson=lesson, name=name, content=content, created_by=request.user
        )

        serializer = CommentSerializer(comment)

        return Response(serializer.data)
