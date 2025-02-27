from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from base.models import User, Employee, Department

APP_NAME = "DRF-Trial"

admin.site.site_header = APP_NAME
admin.site.site_title = APP_NAME
admin.site.index_title = APP_NAME

admin.site.register(User, UserAdmin)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "department",
    )
    list_filter = ("department",)
    search_fields = ("first_name", "last_name", "department__name")
    date_hierarchy = "created_at"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"
