
from report_app.models import Report
from report_app.api.serializers import ReportSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from report_app.api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly




class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class =ReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user', 'category','status']
    
    
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
