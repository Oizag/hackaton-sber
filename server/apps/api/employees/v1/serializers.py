from rest_framework import serializers
from apps.api.employees.models import (
  Employee,
  Schedule
)


class EmployeeAPI(serializers.ModelSerializer):
    class Meta:
      model = Employee
      fields = "__all__"

class ScheduleAPI(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"