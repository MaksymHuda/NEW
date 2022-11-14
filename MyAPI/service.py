from django_filters import rest_framework as filters

from .models import Doctors


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class DoctorsFilter(filters.FilterSet):
    directions = CharFilter(field_name='directions__name', lookup_expr='in')
    work_experience = filters.RangeFilter()

    class Meta:
        model = Doctors
        fields = ['directions', 'work_experience']
