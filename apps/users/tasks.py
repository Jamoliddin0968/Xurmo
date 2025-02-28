from celery import shared_task

from apps.users.models import WorkingDay


@shared_task
def write_numbers():
    WorkingDay.create_new_working_day()
