from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import OlympicsData

class OlympicsViewSet(viewsets.ModelViewSet):
    queryset = OlympicsData.objects.all()
    serializer_class = OlympicsSerializer