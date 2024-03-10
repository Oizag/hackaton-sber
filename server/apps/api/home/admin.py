from django.contrib import admin
from .models.projects import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "progress", "deadline", "status"]
    prepopulated_fields = {"slug": ("name",)}
