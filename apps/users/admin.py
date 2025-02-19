from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "first_name", "last_name", "position", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha Ma'lumotlar", {"fields": ("birth_date", "position", "address")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "classes": ("wide",),
            "fields": ("birth_date", "position", "address"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
