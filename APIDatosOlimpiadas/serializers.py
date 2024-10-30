from rest_framework import serializers
from .models import *

class OlympicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympicsData
        fields = ('__all__')