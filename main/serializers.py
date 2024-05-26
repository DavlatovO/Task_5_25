from rest_framework import serializers
from .import models
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModels
        fields = '__all__'
        
