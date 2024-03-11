from rest_framework import views, generics
from .serializers import (
  EmployeeAPI,
  ScheduleAPI
)
from apps.api.employees.models import (
  Employee,
  Schedule
)
from rest_framework.permissions import AllowAny

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeAPI
    permission_classes = (AllowAny,)

class EmployeeAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeAPI
    permission_classes = (AllowAny,)

class ScheduleListAPIView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleAPI
    permission_classes = (AllowAny,)

class ScheduleAPIView(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleAPI
    permission_classes = (AllowAny,)

