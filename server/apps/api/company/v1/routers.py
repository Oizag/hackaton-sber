from django.urls import path
from .views import (
  ProjectListAPIView,
  ProjectAPIView,
  ProjectCreateAPIView,
  TaskListAPIView,
  TaskCreateAPIView,
  TaskAPIView
)

app_name = "company"

urlpatterns = [
    path("project/list", ProjectListAPIView.as_view(), name="projects list"),
    path("project/<int:pk>", ProjectAPIView.as_view(), name="project retrieve"),
    path("project/create", ProjectCreateAPIView.as_view(), name="project create"),
    path("task/list", TaskListAPIView.as_view(), name="task list"),
    path("task/<int:pk>", TaskAPIView.as_view(), name="task retrieve"),
    path("task/create", TaskCreateAPIView.as_view(), name="task create")
]
