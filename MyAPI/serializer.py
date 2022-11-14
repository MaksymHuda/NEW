from rest_framework import serializers
from .models import Doctors, Directions


class DirectList(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = ('name',)


class DirectionsListForDoctors(serializers.StringRelatedField):
    class Meta:
        model = Directions
        fields = ('name',)


class DoctorsSerializer(serializers.ModelSerializer):
    directions = DirectionsListForDoctors(many=True)

    class Meta:
        model = Doctors
        fields = ('name', 'slug',
                  'directions', 'description',
                  'work_experience',
                  'birt_date'
                  )
