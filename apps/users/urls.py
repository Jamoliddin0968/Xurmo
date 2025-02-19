from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
