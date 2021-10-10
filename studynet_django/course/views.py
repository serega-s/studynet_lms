from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Comment, Course, Lesson
from .serializers import (CourseDetailSerializer, CourseListSerializer,
                          LessonListSerializer, CommentSerializer)


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
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

    return Response({'message': 'The comment was added!'})
