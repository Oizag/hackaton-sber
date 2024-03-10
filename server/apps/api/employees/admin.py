from django.contrib import admin
from .models import (
  Employee, Schedule
)


# Register your models here.
@admin.register(Employee)
class AdminEpmployee(admin.ModelAdmin):
    list_display = ["name", "email", "project_role", "reservation_status"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    list_display = ["timeline_id", "name", "hours"]
