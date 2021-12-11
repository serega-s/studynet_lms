from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ManyToManyField


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Course(models.Model):
    categories = ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''


class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'

    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz')
    )

    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(
        max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(
        Course, related_name='comments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
