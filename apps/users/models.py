from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


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
        if name == "":
            name = self.username
        return name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


class ATTENDANCE_STATUS_CHOICES(models.TextChoices):
    COME = "come", "Kelgan"
    ABSENT = "absent", "Kelmagan"
    LATE = "late", "Kech kelgan"


class Attendance(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="attendances",
        verbose_name="Xodim")
    date = models.DateField(verbose_name="Sana")
    work_time = models.TimeField(null=True, verbose_name="Ish vaqti")
    arrival_time = models.TimeField(
        null=True, blank=True, verbose_name="Kelish vaqti")
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
