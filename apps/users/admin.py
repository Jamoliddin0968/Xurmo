from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Attendance, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    # list_display = ("username", "email", "first_name", "last_name", "position",)
    fields = ("employee_id", "first_name",
              "last_name",
              "position",
              "work_time", "birth_date",
              "address", "phone", "photo")
    readonly_fields = ("employee_id",)


admin.site.register(CustomUser, CustomUserAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'work_time', 'arrival_time',
                    'late_minutes', 'reason', 'serial_id')
    ordering = ['-id']  # Sort by id in the admin panel
    list_filter = ("user",)
    # readonly_fields = ("user", "date", "work_time",
    #                    "arrival_time", "late_minutes", "status",  "serial_id")


# Register your model with the custom admin class
admin.site.register(Attendance, AttendanceAdmin)
