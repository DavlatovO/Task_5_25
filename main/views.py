from django.shortcuts import render
from . import models
from rest_framework.generics import ListAPIView
from .serializers import NewsSerializer

class NewsAPIView(ListAPIView):
    queryset = models.CarModels.objects.all()
    serializer_class = NewsSerializer