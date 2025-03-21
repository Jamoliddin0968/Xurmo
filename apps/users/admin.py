from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Attendance, AttendanceItems, CustomUser

admin.site.unregister(Group)


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


class AttendanceItemsInline(admin.TabularInline):  # yoki admin.StackedInline
    model = AttendanceItems
    readonly_fields = ("marked_at",)
    can_delete = False
    exclude = ("user", "data", "serial_id")

    def has_add_permission(self, request, obj=None):
        """Admin panelda yangi 'AttendanceItems' qo‘shish imkoniyatini o‘chirish"""
        return False  # Yangi element qo‘shishni cheklash

    # def has_change_permission(self, request, obj=None):
    #     """Mavjud 'AttendanceItems' obyektlarini tahrirlashga ruxsat berish"""
    #     return True


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'work_time', 'arrival_time',
                    'late_minutes', 'left_time',  'status')
    ordering = ['-id']
    list_filter = ("user", "date")
    readonly_fields = ("user", "date", "working_day", "work_time",
                       "arrival_time", "late_minutes", "status", "serial_id", "left_time")
    inlines = [AttendanceItemsInline]  # Inline qo'shish
