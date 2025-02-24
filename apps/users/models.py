from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    work_time = models.TimeField(null=True,)
    employee_id = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"


class ATTENDANCE_STATUS_CHOICES(models.TextChoices):
    COME = "come", "Kelgan"
    ABSENT = "absent", "Kelmagan"
    LATE = "late", "Kech kelgan"


class Attendance(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()  # Sana
    work_time = models.TimeField(null=True)  # Ish vaqti (8:00, 9:00 va h.k.)
    arrival_time = models.TimeField(null=True, blank=True)  # Kelgan vaqti
    late_minutes = models.PositiveIntegerField(
        null=True, blank=True)  # Necha daqiqaga kechikkan
    # Kech kelgan yoki kelmagan sababi
    reason = models.TextField(null=True, blank=True)
    serial_id = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS_CHOICES.choices,
                              default=ATTENDANCE_STATUS_CHOICES.ABSENT)  # Davomat holati

    class Meta:
        # unique_together = ("user", "date")  # Har bir foydalanuvchi uchun bitta sana bo'lishi kerak
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"

    def __str__(self):
        return f"{self.user.first_name} - {self.date} - {self.arrival_time or 'Kelmagan'}"
