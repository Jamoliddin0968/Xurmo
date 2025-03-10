from datetime import datetime, time

from django.core.management.base import BaseCommand

from apps.users.models import Attendance, CustomUser, WorkingDay


class Command(BaseCommand):
    help = 'Create test data'

    def handle(self, *args, **options):
        working_day = WorkingDay.create_new_working_day()
        for user in CustomUser.objects.all().exclude(is_superuser=True):
            Attendance.objects.create(
                user=user, working_day=working_day, date=datetime.now().date())
