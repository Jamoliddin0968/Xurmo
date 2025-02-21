from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "birth_date", "position","work_time", "address")

from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Attendance
        fields = ["id", "user", "user_full_name", "date", "work_time", "arrival_time", "late_minutes", "reason"]

