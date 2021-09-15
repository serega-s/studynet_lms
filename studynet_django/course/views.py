from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CourseListSerializer
from .models import Category, Course


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)
