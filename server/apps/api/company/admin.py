from django.contrib import admin
from .models import (
  Project,
  Task
)


# Register your models here.
@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = [
        "name",
        "cost",
        "perspective",
        "progress",
        "start_date",
        "deadline_date",
        "status",
    ]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = [
      "title",
      "descripion",
      "task_start",
      "task_end",
      "status",
      "project"
    ]
