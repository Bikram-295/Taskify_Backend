from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

def home(request):
    return JsonResponse({
        "status": "OK",
        "message": "Taskify Backend is running"
    })

urlpatterns = [
    path("", home),  # 👈 ROOT HEALTH CHECK
    path("admin/", admin.site.urls),
    path("taskify/", include("Taskify_App.urls")),
    path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
]
