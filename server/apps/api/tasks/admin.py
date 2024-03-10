from django.contrib import admin
from .models.task import Task

# Register your models here.
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ["title", "type_task", "task_end", "status", "project", "assigned_to"]