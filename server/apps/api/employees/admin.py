from django.contrib import admin
from .models.employee_detail import Employee

# Register your models here.
@admin.register(Employee)
class AdminEpmployee(admin.ModelAdmin):
    list_display = ["name", "email", "project_role", "reservation_status"]
    prepopulated_fields = {"slug": ("name",)}
