from django.contrib import admin
from .models.project import Project


# Register your models here.
@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = [
        "name",
        "cost",
        "progress",
        "start_date",
        "deadline_date",
        "status",
    ]
    prepopulated_fields = {"slug": ("name",)}
