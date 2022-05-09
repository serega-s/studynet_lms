from rest_framework.response import Response
from rest_framework.views import APIView

from activity.models import Activity
from activity.serializers import ActivitySerializer
from course.models import Course, Lesson
from course.serializers import CourseListSerializer


class GetActiveCoursesListAPIView(APIView):
    def get(self, request):
        courses = []
        activities = Activity.objects.select_related('course', 'lesson', 'created_by').filter(
            created_by=request.user, status=Activity.STARTED
        )

        for activity in activities:
            if activity.course not in courses:
                courses.append(activity.course)

        serializer = CourseListSerializer(courses, many=True)

        return Response(serializer.data)


class TrackStartedAPIView(APIView):

    def post(self, request, course_slug, lesson_slug):
        course = Course.objects.get(slug=course_slug)
        lesson = Lesson.objects.get(slug=lesson_slug)
        if not Activity.objects.select_related('course', 'lesson', 'created_by').filter(
                created_by=request.user, course=course, lesson=lesson
        ).exists():
            Activity.objects.create(created_by=request.user, course=course, lesson=lesson)

        activity = Activity.objects.select_related('course', 'lesson', 'created_by').get(
            created_by=request.user, course=course, lesson=lesson
        )

        serializer = ActivitySerializer(activity)

        return Response(serializer.data)


class MarkAsDoneAPIView(APIView):

    def post(self, request, course_slug, lesson_slug):
        course = Course.objects.get(slug=course_slug)
        lesson = Lesson.objects.get(slug=lesson_slug)

        activity = Activity.objects.select_related('course', 'lesson', 'created_by').get(
            created_by=request.user, course=course, lesson=lesson
        )
        activity.status = Activity.DONE
        activity.save()

        serializer = ActivitySerializer(activity)

        return Response(serializer.data)
