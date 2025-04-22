from django.urls import path
from . import views

urlpatterns = [
    path('recent/', views.recent_notifications),
    path('all/', views.all_notifications),
    path('mark-read/<uuid:notification_id>/', views.mark_as_read),
    path('unread-count/', views.unread_count),
]