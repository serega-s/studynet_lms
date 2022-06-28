from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Category, Comment, Course, Lesson
from course.serializers import (CategorySerializer, CommentSerializer,
                                CourseDetailSerializer, CourseListSerializer,
                                LessonListSerializer, QuizSerializer,
                                UserSerializer)


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
        course = Course.objects.filter(status=Course.PUBLISHED).get(slug=slug)
        course_serializer = CourseDetailSerializer(course)
        lesson_serializer = LessonListSerializer(
            course.lessons.all(), many=True)

        course_data = course_serializer.data if request.user.is_authenticated else {}
        return Response(
            {
                'course': course_data,
                'lessons': lesson_serializer.data
            }
        )


class AuthorCourseListAPIView(APIView):
    def get(self, request, user_id):
        courses = Course.objects.prefetch_related(
            'categories').select_related('created_by').filter(created_by=user_id, status=Course.PUBLISHED).order_by('-created_at')
        user = User.objects.get(pk=user_id)
        courses_serializer = CourseListSerializer(courses, many=True)
        user_serializer = UserSerializer(user)

        return Response(
            {
                'courses': courses_serializer.data,
                'created_by': user_serializer.data
            }
        )


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.prefetch_related(
        'categories').select_related('created_by').filter(status=Course.PUBLISHED).order_by('-created_at')
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = CourseListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # type: ignore
        if category_id := self.request.query_params.get('category_id'):
            queryset = queryset.filter(categories__in=[int(category_id)])

        if limit := self.request.query_params.get('limit'):  # type: ignore
            queryset = queryset[:int(limit)]

        return queryset


class GetCommentsAPIView(APIView):
    def get(self, request, course_slug, lesson_slug):
        lesson = Lesson.objects.select_related('course').get(slug=lesson_slug)
        serializer = CommentSerializer(lesson.comments.all(), many=True)
        return Response(serializer.data)


class AddCommentAPIView(APIView):
    def post(self, request, course_slug, lesson_slug):
        data = request.data
        name = data['name']
        content = data['content']
        lesson = Lesson.objects.get(slug=lesson_slug)

        comment = Comment.objects.create(
            lesson=lesson, name=name, content=content, created_by=request.user
        )

        serializer = CommentSerializer(comment)

        return Response(serializer.data)


class CreateCourseAPIView(APIView):
    def post(self, request):
        status = request.data.get('status'),

        if status == 'published':
            status = 'draft'

        course = Course.objects.create(
            title=request.data.get('title'),
            short_description=request.data.get('short_description'),
            long_description=request.data.get('long_description'),
            status=status,
            created_by=request.user
        )

        for id in request.data.get('categories'):
            course.categories.add(id)

        lessons_data = request.data.get('lessons')

        for lesson_obj in lessons_data:
            lesson_obj.update({**lesson_obj, 'status': Lesson.DRAFT})

            lessons = [Lesson(**lesson_obj, course_id=course.id)]

        Lesson.objects.bulk_create(lessons)

        serializer = CourseDetailSerializer(course)

        return Response(serializer.data)
