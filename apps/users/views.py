from calendar import Calendar, monthrange
from collections import defaultdict
from datetime import date, datetime, time, timedelta, timezone
from json import loads
from uuid import uuid4

from django.db.models import Count, F, Q, Sum
from django.http import HttpRequest
from django.utils.timezone import make_aware
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (ATTENDANCE_STATUS_CHOICES, Attendance, AttendanceItems,
                     CustomUser)
from .schema import Event
from .serializers import AttendanceSerializer, CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().exclude(is_superuser=True)
    serializer_class = CustomUserSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        response_data = self.get_stats(qs=queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data['data'] = serializer.data
        return Response(response_data)

    def get_stats(self, qs):
        result = {}

        target_date = date.today()

        start_of_week = target_date - timedelta(days=target_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        weekly_absent = qs.filter(
            date__range=[start_of_week, end_of_week],
            status=ATTENDANCE_STATUS_CHOICES.ABSENT
        ).count()
        weekly_late_minutes = qs.filter(
            date__range=[start_of_week, end_of_week],
            late_minutes__isnull=False
        ).aggregate(total_late=Sum('late_minutes'))['total_late'] or 0

        start_of_month = target_date.replace(day=1)
        last_day = monthrange(target_date.year, target_date.month)[1]
        end_of_month = target_date.replace(day=last_day)
        monthly_absent = qs.filter(
            date__range=[start_of_month, end_of_month],
            status=ATTENDANCE_STATUS_CHOICES.ABSENT
        ).count()

        monthly_late_minutes = qs.filter(
            date__range=[start_of_month, end_of_month],
            late_minutes__isnull=False
        ).aggregate(total_late=Sum('late_minutes'))['total_late'] or 0

        result = {
            "weekly": {
                "absent_days": weekly_absent,
                "late_minutes": weekly_late_minutes,
            },
            "monthly": {
                "absent_days": monthly_absent,
                "late_minutes": monthly_late_minutes,
            }
        }

        return result


def calculate_late_minutes(event_datetime: datetime, user_work_time: time) -> int:
    """
    Calculates late minutes by comparing event dateTime (arrival time)
    with work_time (expected start time).
    """
    if event_datetime is None or user_work_time is None:
        return 0  # No late time if values are missing
    work_datetime = datetime.combine(
        event_datetime.date(), user_work_time, event_datetime.tzinfo)

    # Calculate late minutes (only if event is after work time)
    late_minutes = max(
        (event_datetime - work_datetime).total_seconds() // 60, 0)
    return int(late_minutes)
    # return int((event_datetime.time()-user_work_time))


class ReceiveDataView(GenericAPIView):
    serializer_class = AttendanceSerializer

    def post(self, *args, **kwargs):
        event = Event.model_validate(self.request.data)
        user_id = event.AccessControllerEvent.employeeNoString
        if not user_id or user_id == "0":
            return Response({"mess": "dfdhub"})
        user = CustomUser.objects.filter(employee_id=user_id).first()
        if not user:
            user = CustomUser.objects.create(
                employee_id=user_id,
                username=f"username_{user_id}_{str(uuid4())}"
            )

        late_minutes = calculate_late_minutes(event.dateTime, user.work_time)
        status = ATTENDANCE_STATUS_CHOICES.COME
        if late_minutes and late_minutes > 0:
            status = ATTENDANCE_STATUS_CHOICES.LATE
        attendance, _ = Attendance.objects.get_or_create(
            user=user,
            date=event.dateTime.date(),
            defaults={
                "date": event.dateTime,
                "work_time": user.work_time,
                "arrival_time": event.dateTime,
                "late_minutes": late_minutes,
                "serial_id": event.AccessControllerEvent.serialNo,
                "status": status
            }
        )
        AttendanceItems.objects.get_or_create(
            serial_id=event.AccessControllerEvent.serialNo,
            defaults={
                "user": user,
                "attendance": attendance,
                "marked_at": event.dateTime,
                "serial_id": event.AccessControllerEvent.serialNo,
                'data': event.model_dump_json()
            }
        )

        return Response({"message": "Attendance updated successfully."}, status=200)
