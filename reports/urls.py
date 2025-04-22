from django.urls import path
from .views import AnalyticListView, dashboard_view

urlpatterns = [
    path('analytics/', AnalyticListView.as_view(), name='analytic-list'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
