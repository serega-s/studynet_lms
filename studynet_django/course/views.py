from rest_framework import permissions
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response

from .models import Category, Comment, Course, Lesson
from .serializers import (CategorySerializer, CommentSerializer,
                          CourseDetailSerializer, CourseListSerializer,
                          LessonListSerializer, QuizSerializer)

@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([permissions.AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([permissions.AllowAny])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.order_by('-created_at').all()

    if category_id:
        courses = Course.objects.filter(categories__in=[int(category_id)])
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([permissions.AllowAny])
def get_frontpage_courses(request):
    courses = Course.objects.order_by('-created_at').all()[0:4]
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([])
@permission_classes([permissions.AllowAny])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    if request.user.is_authenticated:
        course_data = course_serializer.data
    else:
        course_data = {}

    data = {
        'course': course_data,
        'lessons': lesson_serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data['name']
    content = data['content']
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course, lesson=lesson, name=name, content=content, created_by=request.user)

    serializer = CommentSerializer(comment)

    return Response(serializer.data)
