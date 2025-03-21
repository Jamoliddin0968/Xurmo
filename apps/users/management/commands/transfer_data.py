from django.apps import apps
from django.core.management.base import BaseCommand

from apps.users.models import Attendance, AttendanceItems


class Command(BaseCommand):
    help = "Transfer data from SQLite (default) to MySQL (mysql)"

    def handle(self, *args, **options):
        source = 'default'  # SQLite
        target = 'mysql'    # MySQL

        models = [Attendance, AttendanceItems]

        for model in models:
            model_name = model.__name__
            try:
                objects = model.objects.using(source).all()
                total = objects.count()
                self.stdout.write(
                    f"{model_name}: {total} ta obyekt ko'chirilmoqda...")

                for obj in objects:
                    try:
                        obj.pk = None
                        obj.save(using=target)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(
                            f" {model_name} uchun xatolik: {e}"))

                self.stdout.write(self.style.SUCCESS(
                    f" {model_name}: {total} ta obyekt kochirildi."))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f" {model_name} uchun xatolik: {e}"))
