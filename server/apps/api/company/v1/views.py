from rest_framework import views, generics
from rest_framework.permissions import AllowAny
from apps.api.company.models import (
  Project,
  Task
)
from .serializers import (
  ProjectAPI,
  ProjectTasksAPI
)

#############################
# Вьюшки для модели Project #
#############################
class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectAPI
    permission_classes = (AllowAny,)


class ProjectAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectAPI
    permission_classes = (AllowAny,)

class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectAPI
    permission_classes = (AllowAny,)

    # Здесь обращение к алгоритму идет
    # def perfom_create(self, serializer):
    #     serializer.save()

#############################
# Вьюшки для модели Task #
#############################

class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ProjectTasksAPI
    permission_classes = (AllowAny,)


class TaskAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = ProjectTasksAPI
    permission_classes = (AllowAny,)

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ProjectTasksAPI
    permission_classes = (AllowAny,)