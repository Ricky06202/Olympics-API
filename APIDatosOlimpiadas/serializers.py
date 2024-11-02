from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class OlympicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympicsData
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']