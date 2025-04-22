from rest_framework import serializers
from .models import Analytic, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AnalyticSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Analytic
        fields = ['id', 'category', 'average_resolution_time', 'total_reports', 'resolved_reports', 'last_updated']
