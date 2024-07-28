from django.db.models import Count
from rest_framework import generics

from core.courses.models import Subject
from core.courses.api.serializers import SubjectSerializer
from core.courses.api.pagination import StandardPagination


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
