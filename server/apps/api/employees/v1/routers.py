from django.urls import path
from .views import (
  EmployeeListAPIView,
  EmployeeAPIView,
  ScheduleListAPIView,
  ScheduleAPIView
)

app_name = "employees"

urlpatterns = [
    path("list", EmployeeListAPIView.as_view(), name="employees list"),
    path("<int:pk>", EmployeeAPIView.as_view(), name="employees retrieve"),
    path("schedule/list", ScheduleListAPIView.as_view(), name="schedule list"),
    path("schedule/<int:pk>", ScheduleAPIView.as_view(), name="schedule retrieve")
]
