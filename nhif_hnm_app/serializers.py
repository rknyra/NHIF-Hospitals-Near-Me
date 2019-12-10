from .models import Hospital
from rest_framework import serializers

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'location', 'website']