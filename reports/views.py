from rest_framework import generics
from .models import Analytic
from .serializers import AnalyticSerializer
from django.shortcuts import render

class AnalyticListView(generics.ListAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer

def dashboard_view(request):
    return render(request, 'reports/dashboard.html')
