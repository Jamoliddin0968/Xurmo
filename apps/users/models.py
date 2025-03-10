from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(
        max_length=150, blank=True, verbose_name=("Ism"))
    last_name = models.CharField(
        max_length=150, blank=True, verbose_name=("Familiya"))
    birth_date = models.DateField(
        null=True, blank=True, verbose_name="Tug'ilgan sana")
    position = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Lavozim")
    address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Manzil")
    work_time = models.TimeField(null=True, verbose_name="Ish vaqti")
    employee_id = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Xodim ID")
    phone = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name="Telefon raqami")
    photo = models.ImageField(
        upload_to="users/", null=True, blank=True, verbose_name="Rasm")

    def get_rating(self):
        return float(5)

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if not self.first_name:
            return f"user-{self.employee_id}"
        return name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


class ATTENDANCE_STATUS_CHOICES(models.TextChoices):
    COME = "come", "Kelgan"
    ABSENT = "absent", "Kelmagan"
    LATE = "late", "Kech kelgan"


class ATTENDANCE_ITEM_STATUS_CHOICES(models.TextChoices):
    CAME = "came", "Keldi"
    LEFT = "left", "Ketdi"


class WorkingDay(models.Model):
    class DayType(models.TextChoices):
        WORKDAY = 'workday', _('Ish kuni')
        WEEKEND = 'weekend', _('Dam olish kuni')
        HOLIDAY = 'holiday', _('Bayram kuni')

    start_datetime = models.DateTimeField(
        unique=True, verbose_name="Ish kuni boshlanishi")
    end_datetime = models.DateTimeField(verbose_name="Ish kuni tugashi")
    day_type = models.CharField(
        max_length=10,
        choices=DayType.choices,
        default=DayType.WORKDAY,
        verbose_name="Kun turi"
    )
    is_closed = models.BooleanField(default=False, verbose_name="Yopiqmi")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilgan")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Yangilangan")

    class Meta:
        verbose_name = "Рабочий день"
        verbose_name_plural = "Рабочие дни"
        ordering = ['start_datetime']

    def __str__(self):
        return f"{self.start_datetime} - {self.end_datetime} ({self.get_day_type_display()})"

    @classmethod
    def create_new_working_day(cls):
        """Создает новый рабочий день, начиная с 4:00 утра"""
        today = datetime.today().date()
        start_time = datetime.combine(today, datetime.min.time()).replace(
            hour=4, minute=0, second=0)
        end_time = start_time + timedelta(days=1)

        if not cls.objects.filter(start_datetime=start_time).exists():
            return cls.objects.create(start_datetime=start_time, end_datetime=end_time)
        return None

    def is_current_working_day(self):
        """Определяет, находится ли сейчас время в пределах рабочего дня"""
        now = datetime.now()
        return self.start_datetime <= now < self.end_datetime

    @classmethod
    def get_current_working_day(cls):
        """Возвращает текущий рабочий день (если есть), иначе None"""
        now = datetime.now()
        return cls.objects.filter(start_datetime__lte=now, end_datetime__gt=now).first()


class Attendance(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="attendances",
        verbose_name="Xodim")
    working_day = models.ForeignKey(
        WorkingDay, on_delete=models.SET_NULL, related_name="attendances", null=True, blank=True,
        verbose_name="Ish kuni")
    date = models.DateField(verbose_name="Sana", null=True, blank=True)
    work_time = models.TimeField(
        null=True, blank=True, verbose_name="Ish vaqti")
    arrival_time = models.TimeField(
        null=True, blank=True, verbose_name="Kelish vaqti")
    left_time = models.TimeField(
        null=True, blank=True, verbose_name="Ketish vaqti")

    late_minutes = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Kechikish daqiqasi")
    reason = models.TextField(null=True, blank=True, verbose_name="Sabab")
    serial_id = models.PositiveIntegerField(
        null=True, verbose_name="Tartib raqami")
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS_CHOICES.choices,
                              default=ATTENDANCE_STATUS_CHOICES.ABSENT, verbose_name="Holat")

    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = "Davomat"

    def __str__(self):
        return f"{self.user.first_name} - {self.date} - {self.arrival_time or 'Kelmagan'}"


class AttendanceItems(models.Model):
    attendance = models.ForeignKey(
        Attendance, on_delete=models.SET_NULL, related_name="attendances_items",
        verbose_name="Davomat", null=True, blank=True
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="attendances_items",
        verbose_name="Xodim")
    marked_at = models.DateTimeField(verbose_name="Sana")
    serial_id = models.PositiveIntegerField(
        null=True, verbose_name="Tartib raqami")
    status = models.CharField(max_length=20, choices=ATTENDANCE_ITEM_STATUS_CHOICES.choices,
                              default=ATTENDANCE_ITEM_STATUS_CHOICES.LEFT, verbose_name="Holat")

    data = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = "Davomat"
