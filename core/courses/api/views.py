from django.db.models import Count
from rest_framework import generics, viewsets

from core.courses.models import Course, Subject

from core.courses.api.serializers import CourseSerializer, SubjectSerializer
from core.courses.api.pagination import StandardPagination


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination
