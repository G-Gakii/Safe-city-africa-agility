from django.shortcuts import render
from rest_framework import generics
from .models import Analytic
from .serializers import AnalyticSerializer

def dashboard_view(request):
    return render(request, 'dashboard.html')

class AnalyticListView(generics.ListAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer

    def get_queryset(self):
        for analytic in Analytic.objects.all():
            analytic.calculate_metrics()
        return Analytic.objects.all()
