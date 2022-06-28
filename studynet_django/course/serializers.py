from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Comment, Course, Lesson, Quiz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'short_description', 'get_image', 'status']


class CourseDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug',
                  'short_description', 'long_description', 'created_by', 'status']


class CourseActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'slug']


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'slug',
                  'long_description', 'lesson_type', 'youtube_id']


class LessonActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'created_at']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            'id',
            'lesson_id',
            'question',
            'answer',
            'op1',
            'op2',
            'op3'
        ]
