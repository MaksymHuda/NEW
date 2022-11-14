from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .serializer import DoctorsSerializer, DirectList
from .models import Doctors, Directions
from .service import DoctorsFilter


class DoctorsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class DirectionsPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        return response


class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    pagination_class = DoctorsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = DoctorsFilter
    ordering_fields = ['birt_date', 'work_experience']


class DirectViewSet(viewsets.ModelViewSet):
    queryset = Directions.objects.all()
    serializer_class = DirectList
    pagination_class = DirectionsPagination
