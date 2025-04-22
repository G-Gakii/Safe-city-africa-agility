from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
# 

urlpatterns = [
    path("register/",views.createUserList, name="user-register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("users/<int:pk>/",views.user_detail, name="user-detail"),
    
]