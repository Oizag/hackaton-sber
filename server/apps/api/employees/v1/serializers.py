from rest_framework import serializers
from apps.api.employees.models import Employee


# Create your serializers here.
class Meta:
    model = Employee
    fields = "__all__"
