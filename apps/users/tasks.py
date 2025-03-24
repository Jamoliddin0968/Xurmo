from datetime import datetime

from celery import shared_task

from apps.users.models import Attendance, CustomUser, WorkingDay


@shared_task
def write_numbers():
    working_day = WorkingDay.create_new_working_day()
    for user in CustomUser.objects.all().exclude(is_superuser=True):
        if Attendance.objects.filter(user=user, working_day=working_day).exists():
            continue
        Attendance.objects.create(
            user=user, working_day=working_day, date=datetime.now().date())
