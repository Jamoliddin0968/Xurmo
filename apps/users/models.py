from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    work_time = models.TimeField(null=True,)  #

    def __str__(self):
        return f"{self.username} ({self.email})"


from django.db import models
from django.conf import settings

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()  # Sana
    work_time = models.TimeField()  # Ish vaqti (8:00, 9:00 va h.k.)
    arrival_time = models.TimeField(null=True, blank=True)  # Kelgan vaqti
    late_minutes = models.PositiveIntegerField(null=True, blank=True)  # Necha daqiqaga kechikkan
    reason = models.TextField(null=True, blank=True)  # Kech kelgan yoki kelmagan sababi

    class Meta:
        unique_together = ("user", "date")  # Har bir foydalanuvchi uchun bitta sana bo'lishi kerak
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.arrival_time or 'Kelmagan'}"
