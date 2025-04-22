
from report_app.models import Report
from report_app.api.serializers import ReportSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class =ReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id', 'category_id','status']
    
    
    def perform_create(self, serializer):
        # Check if the user is authenticated and assign it to the 'user' field
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # If not authenticated, set the user to None (i.e., null)
            serializer.save(user=None)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer