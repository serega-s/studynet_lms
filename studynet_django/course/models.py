from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = None
        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Category.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:
                count += 1
                slug = f'{slugify(self.title)}-{count}'
                has_slug = Category.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class Course(models.Model):
    DRAFT = 'draft'
    IN_REVIEW = 'in_review'
    PUBLISHED = 'published'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (IN_REVIEW, 'In review'),
        (PUBLISHED, 'Published')
    ]

    categories = ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title

    def get_image(self):
        return settings.WEBSITE_URL + self.image.url if self.image else ''

    def save(self, *args, **kwargs):
        self.slug = None
        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Course.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:
                count += 1
                slug = f'{slugify(self.title)}-{count}'
                has_slug = Course.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)


class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'

    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
        (VIDEO, 'Video')
    )

    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=PUBLISHED
    )
    lesson_type = models.CharField(
        max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE
    )
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.course.title} - "{self.title}"'

    def save(self, *args, **kwargs):
        self.slug = None
        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Lesson.objects.filter(slug=slug).exists()
            count = 1

            while has_slug:
                count += 1
                slug = f'{slugify(self.title)}-{count}'
                has_slug = Lesson.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)


class Comment(models.Model):
    # course = models.ForeignKey(
    #     Course, related_name='comments', on_delete=models.CASCADE
    # )
    lesson = models.ForeignKey(
        Lesson, related_name='comments', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content


class Quiz(models.Model):
    lesson = models.ForeignKey(
        Lesson, related_name='quizzes', on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)
    op1 = models.CharField(max_length=255, null=True)
    op2 = models.CharField(max_length=255, null=True)
    op3 = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f'{self.lesson.course.title} - {self.lesson.title}: {self.question}'

    class Meta:
        verbose_name_plural = 'Quizzes'
