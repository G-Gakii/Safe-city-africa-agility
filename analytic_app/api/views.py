from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analytic_app.models import Analytic
from .serializers import AnalyticSerializer
from rest_framework.permissions import IsAuthenticated

class AnalyticListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        category_id = request.query_params.get('category_id')
        user_id = request.query_params.get('user_id')
        analytics = Analytic.objects.all()
        if category_id:
            analytics = analytics.filter(category_id=category_id)
        if user_id:
            analytics = analytics.filter(user_id=user_id)
        serializer = AnalyticSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)