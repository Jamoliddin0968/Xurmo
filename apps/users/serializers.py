from rest_framework import serializers

from .models import Attendance, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    def get_rating(self, obj) -> float:
        return obj.get_rating()

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name",
                  "birth_date", "position", "work_time", "address", "rating", "photo", "employee_id", "phone")


class AttendanceSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(
        source="user.get_full_name", read_only=True)

    class Meta:
        model = Attendance
        fields = "__all__"
