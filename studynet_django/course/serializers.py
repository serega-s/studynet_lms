from rest_framework import serializers

from .models import Category, Comment, Course, Lesson, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'short_description', 'get_image']


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug',
                  'short_description', 'long_description']


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'slug', 'long_description', 'lesson_type']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'created_at']



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields  = [
            'id',
            'lesson_id',
            'question',
            'answer',
            'op1',
            'op2',
            'op3'
        ]
